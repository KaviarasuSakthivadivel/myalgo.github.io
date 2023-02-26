# 366. Find Leaves of Binary Tree

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example: Given binary tree

          1
         / \
        2   3
       / \     
      4   5
Returns [4, 5, 3], [2], [1].

Explanation:

Removing the leaves [4, 5, 3] would result in this tree:


       1
      / 
     2

Now removing the leaf [2] would result in this tree:
    
    1

Now removing the leaf [1] would result in the empty tree:
    
    []

Returns [4, 5, 3], [2], [1].

### Thoughts
In each level, while doing DFS, if the level is greater than the result list, create a empty list and add it to the result. 
Then append the node.val to the curr - 1 index of the list. 

### Solution
```java
import java.util.LinkedList;
import java.util.List;

public class BinaryTreeLeaves {
    public static List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> result = new LinkedList<>();
        dfs(result, root);
        return result;
    }

    // It will return the level the tree is in.
    private static int dfs(List<List<Integer>> result, TreeNode root) {
        if(root == null) {
            return 0;
        }

        int left = dfs(result, root.left);
        int right = dfs(result, root.right);
        int currentLevel = Math.max(left, right) + 1;
        if(currentLevel > result.size()) {
            result.add(new LinkedList<>());
        }

        result.get(currentLevel - 1).add(root.val);
        return currentLevel;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        System.out.println(findLeaves(root));
    }
}
```