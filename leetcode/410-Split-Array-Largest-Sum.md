# 410. Split Array Largest Sum

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

    Example 1:

    Input: nums = [7,2,5,10,8], m = 2
    Output: 18
    Explanation:
    There are four ways to split nums into two subarrays.
    The best way is to split it into [7,2,5] and [10,8],
    where the largest sum among the two subarrays is only 18.
    Example 2:

    Input: nums = [1,2,3,4,5], m = 2
    Output: 9
    Example 3:

    Input: nums = [1,4,4], m = 3
    Output: 4

## Solution
### Approach

1. Initially, let's break this into a problem of finding whether it is possible to split the array m times with the given sum. Then, we can use this function to solve this problem. 
2. Your search space for this problem is, max(arr) till the sum of the arr which is true when the split ```m``` equal to the length of the array. 
3. Then, use the binary search. 

```java
class Solution {
    public int splitArray(int[] nums, int m) {
        // https://www.youtube.com/watch?v=OmJuyKaGGjs
        
        int n = nums.length;
        int sum = 0;
        int max = 0;
        for(int i = 0; i < n; i++) {
            sum += nums[i];
            max = Math.max(max, nums[i]);
        }
        
        int low = max;
        int high = sum;
        
        // Binary search
        while(low < high) {
            int mid = low + (high - low) / 2;
            
            // reduce the search on the left side
            if(isSumPossible(nums, mid, m)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        
        return low;
    }
    
    private boolean isSumPossible(int[] nums, int sum, int m) {
        int n = nums.length;
        int currSum = 0;
        int splits = 0;
        for(int i = 0; i < n; i++) {
            currSum += nums[i];
            
            if(currSum > sum) {
                currSum = nums[i];
                splits++;
                
                if(splits > m - 1) {
                    return false;
                }
            }
        }
        
        return true;
    }
}
```