![[Design Amazon.mp4 (540p with 30fps).mp4]]

1\. Gathering System Requirements

As with any systems design interview question, the first thing that we want to do is to gather system requirements; we need to figure out what system we're building exactly.

We're designing the e-commerce side of the Amazon website, and more specifically, the system that supports users searching for items on the Amazon home page, adding items to cart, submitting orders, and those orders being assigned to relevant Amazon warehouses for shipment.

We need to handle items going out of stock, and we've been given some guidelines for a simple "stock-reservation" system when users begin the checkout process.

We have access to two smart services: one that handles user search queries and one that handles warehouse order assignment. It's our job to figure out how these services fit into our larger design.

We'll specifically be designing the system that supports amazon.com (i.e., Amazon's U.S. operations), and we'll assume that this system can be replicated for other regional Amazon stores. For the rest of this walkthrough, whenever we refer to "Amazon," we'll be referring specifically to Amazon's U.S. store.

While the system should have low latency when searching for items and high availability in general, serving roughly 10 orders per second in the U.S., we've been told to focus mostly on core functionality.

2\. Coming Up With A Plan

We'll tackle this system by first looking at a high-level overview of how it'll be set up, then diving into its storage components, and finally looking at how the core functionality comes to life. We can divide the core functionality into two main sections:

-   The user side.
-   The warehouse side.

We can further divide the user side as follows:

-   Browsing items given a search term.
-   Modifying the cart.
-   Beginning the checkout process.
-   Submitting and canceliing orders.

3\. High-Level System Overview

Within a region, user and warehouse requests will get round-robin-load-balanced to respective sets of API servers, and data will be written to and read from a SQL database for that region.

We'll go with a SQL database because all of the data that we'll be dealing with (items, carts, orders, etc.) is, by nature, structured and lends itself well to a relational model.

4\. SQL Tables

We'll have six SQL tables to support our entire system's storage needs.

**Items**

This table will store all of the items on Amazon, with each row representing an item.

| itemId: _uuid_ | name: _string_ | description: _string_ | price: _integer_ | currency: _enum_ | other... |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |

**Carts**

This table will store all of the carts on Amazon, with each row representing a cart. We've been told that each user can only have a single cart at once.

| cartId: _uuid_ | customerId: _uuid_ | items: _\[\]{itemId, quantity}_ |
| --- | --- | --- |
| ... | ... | ... |

**Orders**

This table will store all of the orders on Amazon, with each row representing an order.

| orderId: _uuid_ | customerId: _uuid_ | orderStatus: _enum_ | items: _\[\]{itemId, quantity}_ | price: _integer_ | paymentInfo: _PaymentInfo_ | shippingAddress: _string_ | timestamp: _datetime_ | other... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Aggregated Stock**

This table will store all of the item stocks on Amazon that are relevant to users, with each row representing an item. See the **Core User Functionality** section for more details.

| itemId: _uuid_ | stock: _integer_ |
| --- | --- |
| ... | ... |

**Warehouse Orders**

This table will store all of the orders that Amazon warehouses get, with each row representing a warehouse order. Warehouse orders are either entire normal Amazon orders or subsets of normal Amazon orders.

| warehouseOrderId: _uuid_ | parentOrderId: _uuid_ | warehouseId: _uuid_ | orderStatus: _enum_ | items: _\[\]{itemId, quantity}_ | shippingAddress: _string_ |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |

**Warehouse Stock**

This table will store all of the item stocks in Amazon warehouses, with each row representing an {item, warehouse} pairing. The _physicalStock_ field represents an item's actual physical stock in the warehouse in question, serving as a source of truth, while the _availableStock_ field represents an item's effective available stock in the relevant warehouse; this stock gets decreased when orders are assigned to warehouses. See the **Core Warehouse Functionality** section for more details.

| itemId: _uuid_ | warehouseId: _uuid_ | physicalStock: _integer_ | availableStock: _integer_ |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

5\. Core User Functionality

**GetItemCatalog(search)**

This is the endpoint that users call when they're searching for items. The request is routed by API servers to the smart search-results service, which interacts directly with the **items** table, caches popular item searches, and returns the results.

The API servers also fetch the relevant item stocks from the **aggregated\_stock** table.

**UpdateCartItemQuantity(itemId, quantity)**

This is the endpoint that users call when they're adding or removing items from their cart. The request writes directly to the **carts** table, and users can only call this endpoint when an item has enough stock in the **aggregated\_stock** table.

**BeginCheckout() & CancelCheckout()**

These are the endpoints that users call when they're beginning the checkout process and cancelling it. The _BeginCheckout_ request triggers another read of the **aggregated\_stock** table for the relevant items. If some of the items in the cart don't have enough stock anymore, the UI alerts the users accordingly. For items that do have enough stock, the API servers write to the **aggregated\_stock** table and decrease the relevant stocks accordingly, effectively "reserving" the items during the duration of the checkout. The _CancelCheckout_ request, which also gets automatically called after 10 minutes of being in the checkout process, writes to the **aggregated\_stock** table and increases the relevant stocks accordingly, thereby "unreserving" the items. Note that all of the writes to the **aggregated\_stock** are ACID transactions, which allows us to comfortably rely on this SQL table as far as stock correctness is concerned.

**SubmitOrder(), CancelOrder(), & GetMyOrders()**

These are the endpoints that users call when they're submitting and cancelling orders. Both the _SubmitOrder_ and _CancelOrder_ requests write to the **orders** table, and _CancelOrder_ also writes to the **aggregated\_stock** table, increasing the relevant stocks accordingly (_SubmitOrder_ doesn't need to because the checkout process already has). _GetMyOrders_ simply reads from the **orders** table. Note that an order can only be cancelled if it hasn't yet been shipped, which is knowable from the _orderStatus_ field.

6\. Core Warehouse Functionality

On the warehouse side of things, we'll have the smart order-assignment service read from the **orders** table, figure out the best way to split orders up and assign them to warehouses based on shipping addresses, item stocks, and other data points, and write the final warehouse orders to the **warehouse\_orders** table.

In order to know which warehouses have what items and how many, the order-assignment service will rely on the _availableStock_ of relevant items in the **warehouse\_stock** table. When the service assigns an order to a warehouse, it decreases the _availableStock_ of the relevant items for the warehouse in question in the **warehouse\_stock** table. These _availableStock_ values are re-increased by the relevant warehouse if its order ends up being cancelled.

When warehouses get new item stock, lose item stock for whatever reason, or physically ship their assigned orders, they'll update the relevant _physicalStock_ values in the **warehouse\_stock** table. If they get new item stock or lose item stock, they'll also write to the **aggregated\_stock** table (they don't need to do this when shipping assigned orders, since the **aggregated\_stock** table already gets updated by the checkout process on the user side of things).

7\. System Diagram

![[amazon-system-diagram.svg]]

