# 1721. Swapping Nodes in a Linked List
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

### Thoughts

**Naive Approach**

First get the length of the list as `n`. Then, have two pointers, left and right. 
* Move left pointer by k nodes. 
* Move right pointer by n - k nodes. 

This method requires looping through the list node twice. It can be reduced to one. 

**Better Approach**

Have two pointers, `slow` and `fast`. Till `k` becomes `1` move the fast pointer. Cache the fast pointer.

Then slow starts at head and the fast starts at k - 1 nodes, continue till the `fast.next` is not null. 

Now, just swap the slow and fastCache node. 

[Video explanation - Youtube](https://www.youtube.com/watch?v=OZmCvMsFgDA)

### Solution
```java
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        if(head == null || head.next == null) {
            return head;
        }
        
        ListNode slow = head;
        ListNode fast = head;
        
        while(k-- > 1) {
            fast = fast.next;
        }
        
        ListNode fastCache = fast;
        while(fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        
        int temp = slow.val;
        slow.val = fastCache.val;
        fastCache.val = temp;
        return head;
    }
}
```