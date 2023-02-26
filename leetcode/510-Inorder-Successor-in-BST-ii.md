# 510. Inorder Successor in BST II

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node `p` is the node with the smallest key greater than `p.val`.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node.

Follow up: Could you solve it without looking up any of the node’s `values`?

### Thoughts

* If the node has a right child, and hence its successor is somewhere lower in the tree. Go to the right once and then as many times to the left as you could. Return the node you end up with.

* Node has no right child, and hence its successor is somewhere upper in the tree. Go up till the node that is left child of its parent. The answer is the parent.

### Solution
```java
public Node inorderSuccessor(Node x) {
  if (x == null) {
    return null;
  }
  
  // x has right child
  if (x.right != null) {
    x = x.right;
    while (x.left != null) {
      x = x.left; // go to the leftmost node
    }
    return x;
  }
  
  // x has no right child
  while (x.parent != null) {
    if (x.parent.left == x) {
      return x.parent;
    }
    x = x.parent;
  }
  
  return null;  // it is the last node in the inorder list
}
```