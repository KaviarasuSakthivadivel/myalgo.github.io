### Priority Queues

Before introducing a Heap, let's first talk about a Priority Queue.

[Wikipedia](https://en.wikipedia.org/wiki/Priority_queue): a priority queue is an [abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type) similar to a regular [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) or [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) data structure in which each element additionally has a "priority" associated with it. In a priority queue, an element with high priority is served before an element with low priority.

In daily life, we would assign different priorities to tasks, start working on the task with the highest priority and then proceed to the task with the second highest priority. This is an example of a Priority Queue.

A common misconception is that a Heap is the same as a Priority Queue, which is not true. A priority queue is an abstract data type, while a Heap is a data structure. Therefore, a Heap is not a Priority Queue, but a way to implement a Priority Queue.

There are multiple ways to implement a Priority Queue, such as array and linked list. However, these implementations only guarantee O(1) time complexity for either insertion or deletion, while the other operation will have a time complexity of O(N). On the other hand, implementing the priority queue with Heap will allow both insertion and deletion to have a time complexity of O(logN). So, what is a Heap?

In this chapter, we will learn to:

1. Understand the Heap data structure.
2. Understand Max Heap and Min Heap.
3. Understand the insertion and deletion of a Heap.
4. Implement a Heap.

  

### Definition of Heap

According to Wikipedia, a **Heap** is a special type of binary tree. A heap is a binary tree that meets the following criteria:

- Is a **complete binary tree**;
- The value of each node must be **no greater than (or no less than)** the value of its child nodes.

A Heap has the following properties:

- Insertion of an element into the Heap has a time complexity of O(logN);
- Deletion of an element from the Heap has a time complexity of O(logN);
- The maximum/minimum value in the Heap can be obtained with O(1) time complexity.

  

### Classification of Heap

There are two kinds of heaps: **Max Heap** and **Min Heap**.

- Max Heap: Each node in the Heap has a value **no less than** its child nodes. Therefore, the top element (root node) has the **largest** value in the Heap.
    
- Min Heap: Each node in the Heap has a value **no larger than** its child nodes. Therefore, the top element (root node) has the **smallest** value in the Heap.![[1_1_min_max_heap_diagram_new.png]]


## Construct a Heap
  
Constructing a Heap means initializing an instance of a Heap. All methods of Heap need to be performed on an instance. Therefore, we need to initialise an instance before applying the methods. When creating a Heap, we can simultaneously perform the **heapify** operation. Heapify means converting a group of data into a Heap.

```java
// In Java, a Heap is represented by a Priority Queue
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Arrays;

// Construct an empty Min Heap
PriorityQueue<Integer> minHeap = new PriorityQueue<>();

// Construct an empty Max Heap
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

// Construct a Heap with initial elements. 
// This process is named "Heapify".
// The Heap is a Min Heap
PriorityQueue<Integer> heapWithValues= new PriorityQueue<>(Arrays.asList(3, 1, 2));
```

|Heap method|Time complexity|Space complexity|
|---|---|---|
|Construct a Heap|O(N)|O(N)|
|Insert an element|O(logN)|O(1)|
|Get the top element|O(1)|O(1)|
|Delete the top element|O(logN)|O(1)|
|Get the size of a Heap|O(1)|O(1)|


**Heap** is a commonly used data structure in computer science. In this chapter, we will cover several applications of Heap.

1. Heap Sort
2. The Top-K problem
3. The K-th element

## Problems

[[215. Kth Largest Element in an Array]]
[[347. Top K Frequent Elements]]
[[1337. The K Weakest Rows in a Matrix]]
[[1229. Meeting Scheduler]]
[[2402. Meeting Rooms III]]
[[253-Meeting-Rooms-ii]]



