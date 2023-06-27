#  Prefix Sum

In this article, we're going to discuss simple but  
powerful [prefix sum technique](https://en.wikipedia.org/wiki/Prefix_sum):  
one pass + linear time complexity.

> _Prefix sum_ is a sum of the current value with all previous elements  
> starting from the beginning of the structure.

It could be defined for 1D arrays (sum the current value with all the previous  
integers),

![[prefix-sum.png]]

_Figure 1. Prefix sum for 1D array._

for 2D arrays (sum of the current value with the integers above or on the left)

![[prefix-sum-1.png]]

_Figure 2. Prefix sum for 2D array._

or for the binary trees (sum the values of the current node  
and all parent nodes),

![[prefix-sum-2.png]]

### Prefix Sum: How to Use: Number of Continuous Subarrays that Sum to Target

You might want to use the prefix sum technique for the problems  
like "Find a number of _continuous_ subarrays/submatrices/tree paths  
that sum to target".

Before going to the current problem with the tree,  
let's check the idea on a simpler example [Find a number of continuous subarrays that  
sum to target](https://leetcode.com/problems/subarray-sum-equals-k/).

- Use a variable to track the current prefix sum  
    and a hashmap  
    "prefix sum -> how many times was it seen so far".

![[prefix-sum-3.png]]


_Figure 4. Find a number of continuous subarrays that sum to target._

- Parse the input structure and count the requested  
    subarrays/submatrices/tree paths along the way with the help of that hashmap.  
    How to count?

There could be two situations. In situation 1, the  
subarray with the target sum starts from the beginning of the array.  
That means that the current prefix sum is equal to the target sum,  
and we increase the counter by 1.

![[prefix-sum-4.png]]

_Figure 5. Situation 1: The subarray starts from the beginning of the array._

In situation 2, the  
subarray with the target sum starts somewhere in the middle.  
That means we should add to the counter the number of times we have seen  
the prefix sum `curr_sum - target` so far: `count += h[curr_sum - target]`.

The logic is simple: the current prefix sum is `curr_sum`, and some elements  
before the prefix sum was `curr_sum - target`. All the  
elements in between sum up to `curr_sum - (curr_sum - target) = target`.

![[prefix-sum-5.png]]

#### Solution for Number of Continuous Subarrays that Sum to Target

Here is an implementation of the solution for  
[Find a number of continuous subarrays that  
sum to target](https://leetcode.com/problems/subarray-sum-equals-k/).

```java

public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0, currSum = 0;
        HashMap<Integer, Integer> h = new HashMap();
        
        for (int num : nums) {
            // current prefix sum
            currSum += num;
            
            // situation 1:  
            // continuous subarray starts 
            // from the beginning of the array
            if (currSum == k)
                count++;
            
            // situation 2:
            // number of times the curr_sum − k has occured already, 
            // determines the number of times a subarray with sum k 
            // has occured upto the current index
            count += h.getOrDefault(currSum - k, 0);
            
            // add the current sum
            h.put(currSum, h.getOrDefault(currSum, 0) + 1);    
        }
                
        return count;
    }
}

```