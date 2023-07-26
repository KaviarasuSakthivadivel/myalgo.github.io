# 437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

An image: ![gras](/images/leetcode/437-Path-Sum-III.jpeg)

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

### Thoughts
We start recursion for the left and right sub trees and we add it to list while in the recursion. Loop through the list from the end and start adding the elements, if we reached the target, increment the count. 

Refer leetcode for another solution

### Solution
```java
import java.util.ArrayList;

public class PathSumIII {
    private static int count;
    private static ArrayList<Integer> list = new ArrayList<>();
    public static int pathSum(TreeNode root, int sum) {
        pathSumUtilUsingArrayList(root, sum);
        return count;
    }

    private static void pathSumUtilUsingArrayList(TreeNode root, int sum) {
        if(root == null) {
            return;
        }
        pathSumUtilUsingArrayList(root.left, sum);
        pathSumUtilUsingArrayList(root.right, sum);
        int temp = 0;
        for(int i = list.size() - 1; i >= 0 ; i--) {
            temp += list.get(i);
            if(temp == sum) {
                count++;
            }
        }
        list.remove(list.size() - 1);
    }
}

```


Refer - [[560. Subarray Sum Equals K]]

#### Another Method

```java
    public int pathSumAnotherMethod(TreeNode root, int sum) {
        HashMap<Integer, Integer> preSum = new HashMap<Integer, Integer>();
        preSum.put(0, 1);
        
        pathSumHelperUtil(root, 0, sum, preSum);
        
        return count;
    }
    
    public int pathSumHelperUtil(TreeNode root, int currSum, int target, HashMap<Integer, Integer> preSum) {
        
        if(root == null) {
            return 0;
        }
        
        currSum += root.val;
        
        count += preSum.getOrDefault(currSum - target, 0);
        
        preSum.put(currSum, preSum.getOrDefault(currSum, 0) + 1);
        
        pathSumHelperUtil(root.left, currSum, target, preSum);
        pathSumHelperUtil(root.right, currSum, target, preSum);
        
        preSum.put(currSum, preSum.get(currSum) - 1);
        
        return count;
    } 
```