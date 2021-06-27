# 545. Boundary of Binary Tree
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

### Thoughts
First traverse the left side node. If the `root.left` is not null, just add the root node's value to the list. Else If the `root.right` is not null, add `root.val` and traverse the root.right subtree. 

          1
         /\
        2  3
        \
         6           To print 6, we traverse the right subtree if the left subtree is null. 
         /\
        10 11

Secondly, traverse the leaf, Similarly, traverse for the right sub tree. 

### Solution
```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BoundaryTraversal {
    public static List<Integer> traverseBoundary(TreeNode root) {
        if(root == null) {
            return Collections.emptyList();
        }
        List<Integer> list = new ArrayList<>();
        list.add(root.val);

        leftTree(root.left, list);
        leaf(root, list);
        rightTree(root.right, list);
        return list;
    }

    private static void leaf(TreeNode root, List<Integer> list) {
        if(root == null) {
            return;
        }

        leaf(root.left, list);
        if(root.left == null && root.right == null) {
            list.add(root.val);
        }
        leaf(root.right, list);
    }

    private static void leftTree(TreeNode root, List<Integer> list) {
        if(root != null) {
            if(root.left != null) {
                list.add(root.val);
                leftTree(root.left, list);
            } else if(root.right != null) {
                list.add(root.val);
                leftTree(root.right, list);
            }
        }
    }


    private static void rightTree(TreeNode root, List<Integer> list) {
        if(root != null) {
            if(root.right != null) {
                list.add(root.val);
                rightTree(root.right, list);
            } else if(root.left != null) {
                list.add(root.val);
                rightTree(root.left, list);
            }
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(20);
        root.left = new TreeNode(8);
        root.right = new TreeNode(22);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(12);
        root.left.right.left = new TreeNode(10);
        root.left.right.right = new TreeNode(14);
        root.right.right = new TreeNode(25);
        System.out.println(traverseBoundary(root));
    }
}
```
