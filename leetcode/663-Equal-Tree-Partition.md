# 663. Equal Tree Partition
Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 

    Input:
         5
        / \
      10   10
          /  \
         2    3

    Output: True
    Explanation:
        5
       /
      10

    Sum: 15

      10
     /  \
    2    3

    Sum: 15

### Thoughts
Level wise, calculate the sum for the subtree and add it to the root now. Using BFS traversal. 

Then again do the BFS traversal to check the `halfSum = root.val` present in the subtree of the root. 

### Solution
```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class EqualTreePartition {
    public static boolean checkEqualTree(TreeNode root) {
        if(root == null) {
            return false;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        // Insert into the list, level-wise.
        List<TreeNode> list = new ArrayList<>();
        while(!queue.isEmpty()) {
            TreeNode temp = queue.poll();
            list.add(temp);

            if(temp.left != null) {
                queue.offer(temp.left);
            }
            if(temp.right != null) {
                queue.offer(temp.right);
            }
        }

        for(int i = list.size() - 1; i >=0; i--) {
            TreeNode temp = list.get(i);
            temp.val += (temp.left != null ? temp.left.val : 0);
            temp.val += (temp.right != null ? temp.right.val : 0);
        }

        int sum = root.val;
        // We can't partition odd sum tree
        if(sum % 2 != 0) {
            return false;
        }

        queue.offer(root);
        while(!queue.isEmpty()) {
            TreeNode temp = queue.poll();
            if(temp.val == sum / 2) {
                return true;
            }

            if(temp.left != null) {
                queue.offer(temp.left);
            }
            if(temp.right != null) {
                queue.offer(temp.right);
            }
        }
        return false;
    }
    public static void main(String[] args) {
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(10);
        root.right = new TreeNode(10);
        root.right.left = new TreeNode(2);
        root.right.right = new TreeNode(3);
        System.out.println(checkEqualTree(root));
    }
}
```