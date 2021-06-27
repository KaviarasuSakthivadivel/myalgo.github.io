# 285. Inorder Successor in BST
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

### Thoughts

Use morris inorder traversal. Keep the elements in the stack. When the given element is found, `p` the next element in the stack is the inorder successor

### Solution
```java
public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if(root == p) {
            TreeNode currentR = root.right;
            while(currentR != null && currentR.left != null) {
                currentR = currentR.left;
            }
            return currentR;
        } else if(root.val < p.val) {
            return inorderSuccessor(root.right, p);
        } else {
            return inorderSuccessor(root.left, p);
        }
    }

public TreeNode inorderSuccessorIterative(TreeNode root, TreeNode p) {
    TreeNode res = null;
    TreeNode target = null;
    Stack<TreeNode> stack = new Stack<>();

    while(!stack.isEmpty() || root != null){
        while(root != null){
            stack.push(root);
            root = root.left;
        }

        TreeNode top = stack.pop();
        if(target != null){
            res = top;
            break;
        }
        if(p == top){
            target = top;
        }

        root = top.right;
    }

    return res;
}
```