[[285-Inorder-Successor-in-BST]]
[[1038. Binary Search Tree to Greater Sum Tree]]


## Kth largest Element 

### Using In order morris

```java
private TreeNode KthLargest(TreeNode root, int k) {
    TreeNode curr = root;
    TreeNode Klargest = null;
    // count variable to keep count of visited Nodes
    int count = 0;
    while (curr != null) {
        // if right child is NULL
        if (curr.right == null) {
            // first increment count and check if count = k
            if (++count == k)
                Klargest = curr;
            // otherwise move to the left child
            curr = curr.left;
        } else {
            // find inorder successor of current Node
            TreeNode succ = curr.right;
            while (succ.left != null && succ.left != curr)
                succ = succ.left;

            if (succ.left == null) {
                // set left child of successor to the
                // current Node
                succ.left = curr;
                // move current to its right
                curr = curr.right;
            }
            // restoring the tree back to original binary
            // search tree removing threaded links
            else {
                succ.left = null;
                if (++count == k)
                    Klargest = curr;
                // move current to its left child
                curr = curr.left;
            }
        }
    }
    return Klargest;
}
```


### Given array using BST to solve Kth largest

```java
static int kthLargest(TreeNode root, int k) {
    counter = k;
    inOrder(root);
    return node;
}

static void inOrder(TreeNode root) {
    if (root.right != null) {
        inOrder(root.right);
    }

    counter--;
    if (counter == 0) {
        node = root.data;
        return;
    }

    if (root.left != null) {
        inOrder(root.left);
    }
}

static TreeNode createBST(TreeNode root, int val) {
    if (root == null) {
        return new TreeNode(val);
    }
    if (val < root.data) {
        root.left = createBST(root.left, val);
    } else {
        root.right = createBST(root.right, val);
    }
    return root;
}

public static void main(String args[]) {
    int arr[] = { 10, 20, 30, 40, 50 };
    int arrSize = arr.length;

    TreeNode root = null;

    for (int i = 0; i < arrSize; i++) {
        root = createBST(root, arr[i]);
    }

    int k = 2;

    int kthSmallestEle = kthLargest(root, k);
    System.out.println("Kth Largest element is " + kthSmallestEle);
}
```