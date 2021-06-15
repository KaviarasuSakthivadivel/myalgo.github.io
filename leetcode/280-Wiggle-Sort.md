# 280. Wiggle Sort
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

    the pattern is number in odd position is peak.
First try to solve it without in-place:

### Thoughts

sort the array in increasing order.
create a result array of the same size.
keep 2 pointers, one from the beginning, one from the middle(notice odd/even of array).
put beginning first, then the middle pointer, into the result array.
Solve it in-place.

### Solution
```java
public class Solution {
    public void wiggleSort(int[] nums) {
        if(nums.length<2)  return;

        Arrays.sort(nums);
        for(int i = 2 ;i < nums.length - 1 ; ) {
            int x = nums[i];
            nums[i] = nums[i+1];
            nums[i+1] = x;
            i +=2;
        }       
    }
}
```