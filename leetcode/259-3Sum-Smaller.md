# 259. 3Sum Smaller

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

    For example, given nums = [-2, 0, 1, 3], and target = 2. Return 2. 

Because there are two triplets which sums are less than 2: [-2, 0, 1] [-2, 0, 3] 

Follow up: Could you solve it in O(n2) runtime?

#### Thoughts
Even though sorting scrambles the indice, however it doesn't change the number of good triplet.


#### Solution
```java
import java.util.Arrays;

public class ThreeSumSmaller {
    public static int threeSumSmaller(int[] nums, int target) {
        Arrays.sort(nums);
        int count = 0;
        for(int i = 0; i < nums.length - 2; i++) {
            int left = i + 1;
            int right = nums.length - 1;
            while(left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if(sum < target) {
                    count += (right - left);
                    left++;
                } else {
                    right--;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(threeSumSmaller(new int[]{-2, 0, 1, 3}, 2));
    }
}

```