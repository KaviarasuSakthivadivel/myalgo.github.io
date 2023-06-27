### Consistent Hashing: An Overview and Implementation in Java
###  Introduction
Hashing is a fundamental concept in computer science that is used to transform input data into a fixed-size output called a hash value. Hashing is used in many applications, including data storage, searching, and cryptography. Traditional hashing algorithms can be limited in distributed systems due to the need for rebalancing data when the number of servers changes. In this article, we’ll explore consistent hashing, a technique that addresses some of the limitations of traditional hashing in distributed systems. We’ll also provide a sample implementation of consistent hashing in Java.

### Traditional Hashing and Its Limitations
In traditional hashing, a hash function is used to map each input data item to a fixed-size hash value. The hash value is then used as an index into an array or hash table to store or retrieve data. The main limitation of traditional hashing in distributed systems is that the number of servers can change, which requires rebalancing the data to ensure that it is evenly distributed across the servers. This can be time-consuming and may require moving a large amount of data.

### Introducing Consistent Hashing
Consistent hashing is a technique that addresses the limitations of traditional hashing in distributed systems. In consistent hashing, a hash ring is used to map the hash values to servers. Each server is represented as a point on the ring, and each data item is mapped to the closest server on the ring in a clockwise/anti-clockwise direction. Consistent hashing also uses virtual nodes, which are additional points on the ring that are used to balance the load across the servers.

To implement consistent hashing, a consistent hash function is used to map each data item to a point on the hash ring. The consistent hash function takes the data item as input and returns a hash value between 0 and 2³² — 1. The hash value is then mapped to a point on the ring, which is the closest point in a clockwise direction. If a server is added or removed from the ring, only the data items that are mapped to that server and its closest neighbors on the ring need to be moved, which minimizes the need for rebalancing.

### Advantages and Applications of Consistent Hashing
Consistent hashing has several advantages over traditional hashing in distributed systems.

First, consistent hashing is fault-tolerant, which means that if a server fails or is removed from the ring, only the data items that are mapped to that server and its closest neighbors need to be moved.

Second, consistent hashing is load-balancing, which means that the data is distributed evenly across the servers on the ring.

Finally, consistent hashing is scalable, which means that new servers can be added to the ring without requiring rebalancing of the existing data.

### Real-world examples of consistent hashing in action include:

In content delivery networks (CDNs), consistent hashing is used to distribute content across multiple servers. This ensures that requests for the same content are served by the same server, reducing latency and improving performance (In a content delivery network, consistent hashing is used to map the content to the closest server to reduce the latency).

In databases, consistent hashing is used to shard data across multiple nodes. This allows for horizontal scaling and improves performance by reducing the load on individual nodes.

In caching systems, consistent hashing is used to distribute cache entries across multiple servers. In a distributed caching system, consistent hashing is used to map the cached data to the closest cache server on the ring. This improves cache hit rates and reduces the load on individual servers

Implementation Details
To implement consistent hashing in Java, we’ll use the TreeMap class to represent the hash ring. The TreeMap class is a sorted map that maps the hash values to server names. We'll use the MD5 hash function to generate the hash values, which is a widely-used hash function that produces a 128-bit hash value. To add a server to the ring, we'll generate multiple virtual nodes for that server and add them to the ring. We’ll also use a hash function to generate the name of the virtual node by appending a unique identifier to the server name.

Here’s some sample code to illustrate how to implement consistent hashing in Java:

```java
package com.ishan.system_design;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.*;

public class ConsistentHashing {
    private final TreeMap<Long, String> ring;
    private final int numberOfReplicas;
    private final MessageDigest md;

    public ConsistentHashing(int numberOfReplicas) throws NoSuchAlgorithmException {
        this.ring = new TreeMap<>();
        this.numberOfReplicas = numberOfReplicas;
        this.md = MessageDigest.getInstance("MD5");
    }

    public void addServer(String server) {
        for (int i = 0; i < numberOfReplicas; i++) {
            long hash = generateHash(server + i);
            ring.put(hash, server);
        }
    }

    public void removeServer(String server) {
        for (int i = 0; i < numberOfReplicas; i++) {
            long hash = generateHash(server + i);
            ring.remove(hash);
        }
    }

    public String getServer(String key) {
        if (ring.isEmpty()) {
            return null;
        }
        long hash = generateHash(key);
        if (!ring.containsKey(hash)) {
            SortedMap<Long, String> tailMap = ring.tailMap(hash);
            hash = tailMap.isEmpty() ? ring.firstKey() : tailMap.firstKey();
        }
        return ring.get(hash);
    }

    private long generateHash(String key) {
        md.reset();
        md.update(key.getBytes());
        byte[] digest = md.digest();
        long hash = ((long) (digest[3] & 0xFF) << 24) |
                ((long) (digest[2] & 0xFF) << 16) |
                ((long) (digest[1] & 0xFF) << 8) |
                ((long) (digest[0] & 0xFF));
        return hash;
    }

    public static void main(String[] args) throws NoSuchAlgorithmException {
        ConsistentHashing ch = new ConsistentHashing(3);
        ch.addServer("server1");
        ch.addServer("server2");
        ch.addServer("server3");

        System.out.println("key1: is present on server: " + ch.getServer("key1")); 
        System.out.println("key67890: is present on server: " + ch.getServer("key67890")); 

        ch.removeServer("server1");
        System.out.println("After removing server1");

        System.out.println("key1: is present on server: " + ch.getServer("key1")); 
        System.out.println("key67890: is present on server: " + ch.getServer("key67890")); 
    }
}
```

This implementation uses the TreeMap class to represent the hash ring, with the key being the hash value and the value being the server name. The numberOfReplicas variable specifies the number of virtual nodes to generate for each server, and the MD5 hash function is used to generate the hash values. The addServer method adds a server to the hash ring by generating virtual nodes for it and inserting them into the TreeMap. The removeServer method removes a server from the hash ring by removing all of its virtual nodes from the TreeMap. The getServer method retrieves the server to which a particular key belongs by finding the virtual node with a hash value greater than or equal to the hash value of the key and returning the name of the corresponding server.