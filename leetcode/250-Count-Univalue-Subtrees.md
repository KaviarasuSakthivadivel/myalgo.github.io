# 250. Count Univalue Subtrees

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example: Given binary tree,

              5
             / \
            1   5
           / \   \
          5   5   5 returns 4.
### Thoughts
[DCP question](https://www.dailycodingproblem.com/solution/8?token=53ebbb2dbe35193656837876c84fdf7633daceefc5141fa92ee69ebc45a1ec62f043ef3e)

[Youtube](https://www.youtube.com/watch?v=7HgsS8bRvjo&ab_channel=CSDojo)

### Solution
```java
public class CountUnivalue {

    // O(n ^2) solution
    private static boolean isUnival(TreeNode root) {
        if(root == null) {
            return true;
        }

        if(root.left != null && root.left.val != root.val) {
            return false;
        }

        if(root.right != null && root.right.val != root.val) {
            return false;
        }

        return isUnival(root.left) && isUnival(root.right);
    }

    private static int countUniVal(TreeNode root) {
        if(root == null) {
            return 0;
        }
        int left = countUniVal(root.left);
        int right = countUniVal(root.right);

        if(isUnival(root)) {
            return 1 + left + right;
        }
        return left + right;
    }

    public static void main(String[] args) {
        // O(n ^2) solution
        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.right = new TreeNode(0);
        root.right.left = new TreeNode(1);
        root.right.right = new TreeNode(0);

        root.right.left.left = new TreeNode(1);
        root.right.left.right = new TreeNode(1);

        System.out.println(countUniVal(root));
    }
}

```

O(n) Solution 

```python
def count_unival_subtrees(root):
    count, _ = helper(root)
    return count

# Also returns number of unival subtrees, and whether it is itself a unival subtree.
def helper(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count, False
```