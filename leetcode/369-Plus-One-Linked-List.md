# 369. Plus One Linked List

Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example:

    Input:
    1->2->3

    Output:
    1->2->4

### Thoughts
Create a sentinal head, the idea here is, sentinal head will be used for carry, eg. 999, if we add one, it will be 1000. So, sentinal head will contain 1. Recursive call to `carry` function where it will recur through till the end and it will return `1` if the current node is null and it will update the current nodes value. 

    eg, next = carry(1)

    next = carry(2)

    next = carry(3)
    
    next = carry(null) which will return 1 and the previous node value will be updated in the recursive call. 

### Solution
```java
public class Solution {
    public ListNode plusOne(ListNode head) {
        ListNode fakeHead = new ListNode(0);
        fakeHead.next = head;
        carry(fakeHead);
        if (fakeHead.val != 0) {
            return fakeHead;
        }
        return fakeHead.next;
    }
    private int carry(ListNode node) {
        if (node == null) {
            return 1;
        }
        int next = carry(node.next);
        if (next == 0) {
            return 0;
        }
        int tmp = node.val + next;
        node.val = tmp % 10;
        return tmp / 10;
    }
}
```