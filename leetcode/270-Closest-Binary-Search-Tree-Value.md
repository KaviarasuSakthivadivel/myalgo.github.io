# 270. Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note: Given target value is a floating point. You are guaranteed to have only one unique value in the BST that is closest to the target.


### Thoughts
If root.val is greater than target value, the right subtree can't be closer than root/left subtree.

### Solution
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int closestValue(TreeNode root, double target) {
        TreeNode child = root.val < target ? root.right : root.left;
        if(child == null) return root.val;
        int childClose = closestValue(child, target);
        return Math.abs(target-childClose) > Math.abs(target-root.val) ? root.val : childClose;
    }
}
```