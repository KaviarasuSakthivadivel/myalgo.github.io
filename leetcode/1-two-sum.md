# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Thoughts
1. We have use HashMap to check if the complement is present while running the loop for the array. 

2. We can sort the array and do binary search for the target number. Start from left and right corner, 
Calculate currentSum = arr[left] + arr[right];
If the currentSum is greater than the target, decrement the right pointer down, since the array is sorted, the current sum will get decreased. 
If the currentSum is lesser than the target, increment the left point up, so that you will get a bigger sum. 
When the currentSum is equal to the target, return the left and right pointer elements. 

## Solution
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if(map.containsKey(complement)) {
                return new int[] {map.get(complement) , i};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No solution.");
    }
    
    public int[] twoSumSlidingWindow(int[] nums, int target) {
        // Two pointer approach, we can use this method when the array is sorted. 
        int left = 0, n = nums.length , right = n - 1;
        Arrays.sort(nums);
        while(left < right) {
            int currentSum = nums[left] + nums[right];
            
            if(currentSum == target) {
                return new int[] {left , right};
            }
            
            if(currentSum > target) {
                right--;
            } else {
                left++;
            }
        }
        
        throw new IllegalArgumentException("No solution.");
    }
}
```