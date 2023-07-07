
# 742. Closest Leaf in a Binary Tree

Given the `root` of a binary tree where every node has **a unique value** and a target integer `k`, return _the value of the **nearest leaf node** to the target_ `k` _in the tree_.

**Nearest to a leaf** means the least number of edges traveled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

**Input:** root = [1,2,3,4,null,null,null,5,null,6], k = 2
**Output:** 3
**Explanation:** The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.

![[closest3-tree.jpeg]]

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int findClosestLeaf(TreeNode root, int k) {
        HashMap<TreeNode, List<TreeNode>> graph = new HashMap<>();

        // convert it to a graph and do BFS
        dfs(graph, root, null);

        HashSet<TreeNode> seen = new HashSet<>();
        Queue<TreeNode> queue = new LinkedList<>();
        for(TreeNode node : graph.keySet()) {
            if(node != null && node.val == k) {
                queue.add(node);
                seen.add(node);
            }
        }

        while(!queue.isEmpty()) {
            TreeNode node = queue.poll();

            if(node != null) {
                if(graph.get(node).size() <= 1) { // Has only one outbound, then it is a leaf
                    return node.val;
                }
                for(TreeNode n : graph.get(node)) {
                    if(!seen.contains(n)) {
                        queue.add(n);
                        seen.add(n);
                    }
                }
            }
        }

        return 0;
    }

    private void dfs(HashMap<TreeNode, List<TreeNode>> graph, TreeNode root, TreeNode parent) {
        if(root == null) {
            return;
        }
        graph.computeIfAbsent(root, l -> new LinkedList<>()).add(parent);
        graph.computeIfAbsent(parent, l -> new LinkedList<>()).add(root);

        dfs(graph, root.left, root);
        dfs(graph, root.right, root);
    }
}

```

