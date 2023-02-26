# 217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

### Thoughts


```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hashMap = new HashSet<Integer>();
        
        for(int i = 0 ; i < nums.length ; i++) {
            if(!hashMap.contains(nums[i])) {
                hashMap.add(nums[i]);
            } else {
                return true;
            }
        }
        
        return false;
    }
}
```

