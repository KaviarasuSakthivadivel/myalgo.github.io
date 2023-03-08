# 260. Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

    Example 1:

    Input: nums = [1,2,1,3,2,5]
    Output: [3,5]
    Explanation:  [5, 3] is also a valid answer.
    Example 2:

    Input: nums = [-1,0]
    Output: [-1,0]
    Example 3:

    Input: nums = [0,1]
    Output: [1,0]

### Solution
```java
class Solution {
    public int[] singleNumber(int[] nums) {
        
        int bitMask = 0;
        for(int num : nums) {
            bitMask ^= num;
        }
        
        // Now, the bitmask will contain the diffence in 
        
        // diff - to isolate the rightmost 1-bit, which is different between x and y
        int diff = bitMask & -bitMask;
        
        int x = 0;
        for(int num : nums) {
            if((diff & num) != 0) {
                x ^= num;
            }
        }
        
        return new int[]{x, bitMask ^ x};
    }
}
```