# 298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,

       1
        \
         3
        / \
       2   4
            \
             5
Longest consecutive sequence path is 3-4-5, so return 3.

### Thoughts
Most of the tree problems are solved using recursion. Here, we have a recursive call, which takes in count, that is the current consective sequence nodes in a tree and target will be `root.val + 1` to the next calls. 

[Youtube Explanation](https://www.youtube.com/watch?v=oSYGjIq6ZM4&ab_channel=KevinNaughtonJr.)

### Solution
```java
public class BinaryTreeLongestConsecutiveSequence {
    public static int longestConsecutive(TreeNode root) {
        int[] max = new int[1];
        findlongestConsecutive(root, 0, 0, max);
        return max[0];
    }

    private static void findlongestConsecutive(TreeNode root, int count, int target, int[] max) {
        if(root == null) {
            return;
        } else if(root.val == target) { // Continue incrementing the count if the previous one
            count++;
        } else {
            count = 1; // Reset the count
        }

        max[0] = Math.max(max[0], count);
        findlongestConsecutive(root.left, count, root.val + 1, max);
        findlongestConsecutive(root.right, count, root.val + 1, max);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(2);
        root.right.right = new TreeNode(4);
        root.right.right.right = new TreeNode(5);
        System.out.println(longestConsecutive(root));
    }
}
```