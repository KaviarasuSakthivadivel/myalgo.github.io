Designing a tokenization API for capturing card details in a payment gateway system involves various components, including capacity estimation, API contracts, database designs, algorithms, and security considerations. Let's break down each component and discuss them in detail.

1. Capacity Estimation: Capacity estimation helps determine the resources required to handle the expected load on the API. This involves analyzing factors like the expected number of card capture requests, concurrent users, processing time per request, and average payload size. It helps in provisioning the necessary infrastructure to handle the load efficiently.

To estimate capacity, you can perform load testing by simulating various usage scenarios and measuring response times and resource utilization. This will give you insights into the system's behavior under different loads and help you identify any performance bottlenecks.

1. API Contracts: API contracts define the expectations and obligations for both the API provider and the consumers. In the case of a tokenization API for capturing card details, the contract should include details about request/response formats, data structures, error handling, authentication mechanisms, and security considerations. Here's an example of an API contract for card capture tokenization:

**Request Contract:**

- HTTP Method: POST
- Endpoint: /api/card_capture
- Request Body:
    - card_number: string (required)
    - card_expiration: string (required)
    - card_cvv: string (required)
- Response:
    - Status Code: 200 (Success)
    - Response Body:
        - token: string (the generated card token)
        - expiry_date: string (optional)

1. Database Design: The database design for storing card details and tokens should prioritize security and compliance with payment industry standards. Consider the following aspects:

- **Cards Table**: This table stores the card details, along with the associated token and any additional metadata. It can have columns like **`id`**, **`card_number`**, **`card_expiration`**, **`card_cvv`**, **`token`**, **`created_at`**, etc.
- **Indexing**: Depending on the access patterns, you can create indexes on columns like **`token`**, **`card_number`**, and **`created_at`** to optimize search and retrieval operations.

It's crucial to implement strong encryption mechanisms to protect card details stored in the database. Follow best practices and compliance standards like PCI-DSS (Payment Card Industry Data Security Standard) to ensure the security of sensitive cardholder data.

1. Algorithms: Tokenization algorithms for capturing card details should focus on securely generating unique tokens while maintaining the ability to link tokens back to the original card information. Here's an example of a tokenization algorithm for card details:

```python
import hashlib
import secrets

def generate_card_token(card_number, card_expiration, card_cvv):
    # Concatenate card details
    card_data = f"{card_number}{card_expiration}{card_cvv}"
    
    # Generate a unique token
    unique_id = secrets.token_hex(16)
    
    # Compute the token by hashing the card data and unique ID
    token = hashlib.sha256((card_data + unique_id).encode()).hexdigest()
    
    return token
```

This algorithm concatenates the card number, expiration date, and CVV, adds a unique ID (generated using the **`secrets`** module), and computes a secure hash (SHA-256) of the combined data. The resulting hash serves as the token.

1. Security Considerations: When designing a tokenization API for capturing card details, security is of utmost importance. Consider the following security measures:

- Transport Layer Security (TLS): Ensure that the API is accessed over HTTPS to encrypt the data transmitted between the client and the server.

To make the tokenization API scalable to handle 1 million requests per second, you need to consider several factors. Here are some key considerations for achieving scalability:

1. Distributed System Architecture: Design the system using a distributed architecture that can horizontally scale across multiple servers. This allows you to handle the increased load and distribute requests across multiple instances.
2. Load Balancing: Implement a load balancer that distributes incoming requests evenly across multiple API server instances. The load balancer should be able to handle high throughput and efficiently route requests to available servers.
3. Horizontal Scaling: Scale horizontally by adding more API server instances to the system. This can be achieved by deploying the application in a cloud environment that supports auto-scaling, allowing the infrastructure to automatically add or remove instances based on the current load.
4. Caching: Implement caching mechanisms to store frequently accessed card tokens in memory. This reduces the load on the database and improves response times for subsequent requests. Consider using in-memory caches like Redis or Memcached to store and retrieve card tokens quickly.
5. Database Scaling: Choose a database solution that can handle high read and write loads. Consider using a distributed database or sharding the data across multiple database instances to distribute the load. Additionally, optimize database queries and utilize appropriate indexes to enhance query performance.
6. Asynchronous Processing: For large-scale throughput, consider implementing asynchronous processing. Instead of processing each request synchronously, you can queue the requests for tokenization and use a message queue system (e.g., RabbitMQ, Apache Kafka) to handle the processing asynchronously. This allows for greater concurrency and scalability.
7. Caching at the API Gateway: Implement caching at the API gateway layer to cache responses for frequently accessed endpoints. This reduces the load on the backend services and improves overall response times.
8. Performance Optimization: Optimize the performance of your tokenization algorithm by evaluating the algorithm's efficiency and making any necessary optimizations. For example, you can utilize parallel processing techniques or distributed computing frameworks to speed up tokenization for large-scale requests.
9. System Monitoring and Scaling: Implement a robust monitoring system that tracks the performance, resource utilization, and health of the API servers, load balancers, and databases. Use metrics and performance data to identify bottlenecks, scale resources, and optimize the system for maximum efficiency.
10. Performance Testing and Benchmarking: Conduct rigorous performance testing and benchmarking to validate the system's scalability and identify any performance limitations. Simulate a load of 1 million requests per second using load testing tools like Apache JMeter or Gatling to ensure the system can handle the desired throughput.

It's important to note that achieving a throughput of 1 million requests per second requires a highly optimized and well-architected system. Proper infrastructure provisioning, load balancing, caching, and database optimization are critical to achieving such high scalability. Additionally, leveraging cloud services and auto-scaling capabilities can provide the flexibility needed to handle dynamic loads.