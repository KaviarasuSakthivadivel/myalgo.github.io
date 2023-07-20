# 146. LRU Cache

Design a data structure that follows the constraints of a **[Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU)**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

**Example 1:**

**Input**
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
**Output**
[null, null, null, 1, null, -1, null, -1, 3, 4]

**Explanation**
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


```java
class LRUCacheUsingInbuilt {
    private LinkedHashMap<Integer, Integer> map; 
    private final int capacity; 
    
    public LRUCacheUsingInbuilt(int totalCapacity) {
        this.capacity = totalCapacity;
        map = new LinkedHashMap<Integer, Integer>(totalCapacity, 0.75f, true) {
            protected boolean removeEldestEntry(Map.Entry eldest) {
                return size() > totalCapacity;
            } 
        }; 
    }
    
    public int get(int key) {
         return map.getOrDefault(key, -1); 
    }
    
    public void put(int key, int value) {
        map.put(key, value); 
    }
}

class LRUCache {
    ListNode head, tail; // Sentinal nodes
    HashMap<Integer, ListNode> map;
    private final int capacity;

    public LRUCache(int totalCapacity) {
        this.capacity = totalCapacity;
        this.map = new HashMap<>();

        // initialise sentinal nodes
        this.head = new ListNode(-1, -1);
        this.tail = new ListNode(-1, -1);
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        if(!map.containsKey(key)) {
            return -1;
        }

        ListNode node = map.get(key);
        remove(node);
        add(node);

        return node.value;
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)) {
            remove(map.get(key));
        }

        ListNode node = new ListNode(key, value);
        map.put(key, node);
        add(node);

        if(map.size() > this.capacity) {
            ListNode nodeToDelete = head.next; // don't remove the sentinal node, that's why I removing the head next
            remove(nodeToDelete); 
            map.remove(nodeToDelete.key);
        }
    }


    // Add the node to the tail
    private void add(ListNode node) {
        ListNode previousTail = tail.prev;
        previousTail.next = node;
        node.prev = previousTail;

        node.next = tail;
        tail.prev = node;
    }

    // Remove the node from head
    private void remove(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}

class ListNode {
    int key;
    int value;
    ListNode prev, next;
    
    public ListNode(int key, int value) {
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}
```

The cleanest way to handle the empty list case is by using **sentinel nodes**.

We will have our `head` and `tail` attributes both set to dummy nodes. The "real" head will be `head.next` and the "real" tail will be `tail.prev`. These dummy nodes sit just "outside" of our linked list. What is the purpose? We never want `head` or `tail` to be `null`.

![[lru-cache-1.png]]

**Algorithm**

**Adding a node to the back of the linked list**

We need to add a node to the end of our linked list whenever we add a new key or update an existing one. Let's write a helper method `add(ListNode node)` that takes a `node` and puts it at the end of our linked list.

This can be done in the following steps:

1. Get the current node at the end of the linked list. This is the "real" tail: `tail.prev`. Let's call it `previousEnd`.
2. `node` is being inserted after `previousEnd`. Therefore, set `previousEnd.next = node`.
3. Now, we set the pointers of `node`. First, `node.prev = previousEnd`.
4. Next, because the "real" tail is before `tail`, we set `node.next = tail`.
5. Finally, we update `tail.prev = node`.

```java
public void add(ListNode node) {
    ListNode previousEnd = tail.prev;
    previousEnd.next = node;
    node.prev = previousEnd;
    node.next = tail;
    tail.prev = node;
}
```

**Removing a node from the linked list**

We need to perform removals when we update/fetch an existing key, or when the data structure exceeds `capacity`. Let's write a helper method `remove(ListNode node)` that removes `node` from the linked list.

This can be done in the following steps:

1. Let's call `nextNode = node.next` and `prevNode = node.prev`. Currently, `nextNode.prev = node` and `prevNode.next = node`. To remove `node` from the linked list, we need to reassign `nextNode.prev = prevNode` and `prevNode.next = nextNode`.
2. We can perform both these reassignments without needing to declare `prevNode` or `nextNode` using the following code:
3. `node.prev.next = node.next`
4. `node.next.prev = node.prev`

> Imagine you have `A <-> B <-> C`. To remove `B`, we need `A` and `C` to become adjacent, i.e. `A <-> C`. Here, `prevNode = A` and `nextNode = C`.

```java
public void remove(ListNode node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
}
```

**The `get(int key)` method**

Now that we have helper methods for adding and removing from our linked list, we can easily implement the `get` and `put` methods using simple logic.

1. Check if `key` exists in the hash map. If not, return `-1`.
2. Get the `node` associated with `key` from the hash map.
3. Move it to the back of the linked list. This can be done by first calling `remove(node)` and then `add(node)`.
4. Return the value associated with `key`, which is `node.val`.

```java
public int get(int key) {
    if (!dic.containsKey(key)) {
        return -1;
    }
    
    ListNode node = dic.get(key);
    remove(node);
    add(node);
    return node.val;
}
```

**The `put(int key, int value)` method**

This method updates `key: value` if it already exists, and inserts `key: value` otherwise. If inserting causes the size to exceed `capacity`, we need to remove the least recently used key (which we know is the head of our linked list).

We can perform the following steps:

1. First, check if `key` already exists in the hash map. If it does, find the node associated with it and call `remove` on it. We are going to move the key to the back of the queue, so we need to first remove it from the linked list.
2. Create a new `node` using `key, value`.
3. Set `key: node` in the hash map.
4. Add `node` to the back of the linked list with `add(node)`.
5. Finally, check if the data structure has exceeded `capacity` by using the hash map's size.
    - If it has, then get the `nodeToDelete` as `head.next`.
    - Delete the node with `remove(nodeToDelete)`.
    - Delete the key from the hash map. The key is `nodeToDelete.key`.

```java
public void put(int key, int value) {
    if (dic.containsKey(key)) {
        ListNode oldNode = dic.get(key);
        remove(oldNode);
    }
    
    ListNode node = new ListNode(key, value);
    dic.put(key, node);
    add(node);
    
    if (dic.size() > capacity) {
        ListNode nodeToDelete = head.next;
        remove(nodeToDelete);
        dic.remove(nodeToDelete.key);
    }
}
```

