# Max Uncrossed Lines

## Problem Statement

Given two rows of blocks (or lists of numbers), find the maximum number of pairs you can connect without crossing any lines.

## Java Solution with 1D Dynamic Programming Array

```java
class Solution {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }
        int[] dp = new int[nums2.length + 1];
        for (int i = 1; i <= nums1.length; i++) {
            int prev = 0, cur = 0;
            for (int j = 1; j <= nums2.length; j++) {
                cur = dp[j];
                if (nums1[i - 1] == nums2[j - 1]) {
                    dp[j] = 1 + prev;
                } else {
                    dp[j] = Math.max(dp[j], dp[j - 1]);
                }
                prev = cur;
            }
        }
        return dp[nums2.length];
    }
}
```

## Java Solution with 2D Dynamic Programming Array
```java

class Solution {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int[][] dp = new int[nums1.length + 1][nums2.length + 1];
        for (int i = 1; i <= nums1.length; i++) {
            for (int j = 1; j <= nums2.length; j++) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[nums1.length][nums2.length];
    }
}
```

## Efficiency
The method using a 1D array for dynamic programming is more space-efficient than the method using a 2D array. This is because the 1D array only needs to store the current and previous rows of the dynamic programming table, while the 2D array stores the entire table. Therefore, the 1D array uses less memory, which can be a significant advantage when dealing with large inputs.

In terms of time complexity, both methods are equivalent. They both have a time complexity of O(n*m), where n is the length of nums1 and m is the length of nums2. This is because both methods perform a constant amount of work for each pair of elements in nums1 and nums2.


## Explain this question like you explain to a 5 year old kid with examples.
Sure, let's imagine you and your friend each have a bunch of colored blocks. You both line up your blocks in a row. Now, you want to connect as many blocks of the same color as possible using straight lines, but there's a rule - the lines can't cross each other.

For example, let's say you have blocks in this order: Red, Blue, Green, Red, Blue. And your friend has blocks in this order: Blue, Green, Red, Blue, Red.

You can connect the first Blue block in your row to the first Blue block in your friend's row. Then, you can connect the Green block in your row to the Green block in your friend's row. After that, you can connect the second Red block in your row to the second Red block in your friend's row. So, you can connect 3 pairs of blocks without crossing any lines.

This is what the problem is asking - given two rows of blocks (or lists of numbers), find the maximum number of pairs you can connect without crossing any lines.


## Input: nums1 = [1,4,2], nums2 = [1,2,4]
## Output: 2


Sure, let's use the blocks analogy again. This time, instead of colors, let's say each block has a number on it. You have blocks with numbers 1, 4, and 2, and your friend has blocks with numbers 1, 2, and 4.

You start with your magic notebook at 0 because you haven't made any connections yet.

Your first block is 1, and your friend's first block is also 1. They're the same, so you can draw a line! You add 1 to the best number of connections you've made so far (which is 0), and write down 1 in your notebook.

Your next block is 4, but your friend's next block is 2. They're not the same, so you can't draw a line. You still write down 1 in your notebook because that's the best you've done so far.

Your next block is 2, and your friend's next block is 4. They're not the same, so you can't draw a line. You still write down 1 in your notebook because that's the best you've done so far.

Now, you go back to the start and try again, but this time, you can skip the first block in your row. Your first block is now 4, and your friend's first block is 1. They're not the same, so you can't draw a line. You still write down 1 in your notebook because that's the best you've done so far.

Your next block is 2, and your friend's next block is 2. They're the same, so you can draw a line! You add 1 to the best number of connections you've made so far (which is 1), and write down 2 in your notebook.

Your next block would be after 2, but you don't have any more blocks. So, you're done!

At the end, the number in your notebook is 2, which is the best number of connections you can make without any lines crossing! So the output is 2.