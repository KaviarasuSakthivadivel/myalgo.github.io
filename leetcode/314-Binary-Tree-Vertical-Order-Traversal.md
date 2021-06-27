# 314. Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Given binary tree [3,9,20,4,5,2,7],
                
         3 
       /   \
      9    20
     / \   / \
    4   5 2   7

return its vertical order traversal as:
[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]

### Thoughts
While inserting the root.left node into the queue, keep the depth as `root.depth - 1` 

While inserting the root.right node into the queue, keep the depth as `root.depth + 1` 

### Solution
```java
import java.util.*;

public class BTVerticalOrderTraversal {
    public static List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> result = new LinkedList<>();
        Queue<QueueNode> queue = new LinkedList<>();
        queue.add(new QueueNode(root, 0));

        HashMap<Integer, List<Integer>> map = new HashMap<>();
        int min = 0, max = 0;

        while(!queue.isEmpty()) {
            QueueNode front = queue.poll();
            int depth = front.depth;

            if(!map.containsKey(depth)) {
                map.put(depth, new ArrayList<>());
            }

            map.get(depth).add(front.node.val);
            min = Math.min(min, depth);
            max = Math.max(max, depth);

            if(front.node.left != null) {
                queue.add(new QueueNode(front.node.left, depth - 1));
            }

            if(front.node.right != null) {
                queue.add(new QueueNode(front.node.right, depth + 1));
            }
        }
        for(int i = min; i <= max; i++) {
            result.add(map.get(i));
        }
        return result;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        System.out.println(verticalOrder(root));
    }

    private static class QueueNode {
        TreeNode node;
        int depth;

        public QueueNode(TreeNode node, int depth) {
            this.node = node;
            this.depth = depth;
        }
    }
}
```