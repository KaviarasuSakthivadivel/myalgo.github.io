# 239. Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation: 
    
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7


### Solution
```java
public int[] maxSlidingWindow(int[] arr, int k) {
    Deque<Integer> list = new LinkedList<>();
    ArrayDeque<Integer> result = new ArrayDeque<>(); // For storing the values
    
    int[] l = new int[arr.length - k + 1];

    for(int i = 0 ; i < k; i++) {
        while(!list.isEmpty() && arr[i] >= arr[list.peekLast()]) {
            list.removeLast();
        }
        list.addLast(i);
    }

    for (int i = k; i < arr.length; i++) {
        if(!list.isEmpty()) {
            result.add(arr[list.peek()]);
        }

        // Removing all the elements indexes which are not in the current window
        while(!list.isEmpty() && list.peek() <= i - k) {
            list.removeFirst();
        }

        // Removing all the smaller elements
        while(!list.isEmpty() && arr[i] >= arr[list.peekLast()]) {
            list.removeLast();
        }
        list.addLast(i);
    }
    if(!list.isEmpty())
        result.add(arr[list.peek()]);
    
    int i = 0;
    for(int a : result) {
        l[i++] = a;
    }
    
    return l;
}
```