
# 896. Monotonic Array

An array is **monotonic** if it is either monotone increasing or monotone decreasing.

An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array `nums` is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array `nums`, return `true` _if the given array is monotonic, or_ `false` _otherwise_.

**Example 1:**

**Input:** nums = [1,2,2,3]
**Output:** true

**Example 2:**

**Input:** nums = [6,5,4,4]
**Output:** true

**Example 3:**

**Input:** nums = [1,3,2]
**Output:** false


### Thoughts

Check the first and last el, and decide if the given array should be checked for ascending or descending case!

```java

class Solution {
    public boolean isMonotonic(int[] nums) {    
        
        boolean isAscending = true;
        int n = nums.length;
        if(n == 1) {
            return true;
        }

        if(nums[0] - nums[n - 1] > 0) {
            isAscending = false;
        }

        if(isAscending) {
            for(int i = 0; i < n - 1; i++) {
                if(nums[i] != nums[i + 1] && nums[i] > nums[i + 1]) {
                    return false;
                }
            }
        } else {
            for(int i = 0; i < n - 1; i++) {
                if(nums[i] != nums[i + 1] && nums[i] < nums[i + 1]) {
                    return false;
                }
            }
        }

        return true;
    }
}

```

