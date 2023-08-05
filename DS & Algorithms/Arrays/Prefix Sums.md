# Prefix Sum: 

**How to Use: Number of Continuous Subarrays that Sum to Target**

You might want to use the prefix sum technique for the problems  
like "Find a number of _continuous_ subarrays/submatrices/tree paths  
that sum to target".

- Use a variable to track the current prefix sum  
    and a hashmap  
    "prefix sum -> how many times was it seen so far".

![[560-1.png]]

_Figure 4. Find a number of continuous subarrays that sum to target._


- Parse the input structure and count the requested  
    subarrays/submatrices/tree paths along the way with the help of that hashmap.  
    How to count?

There could be two situations. In situation 1, the  
subarray with the target sum starts from the beginning of the array.  
That means that the current prefix sum is equal to the target sum,  
and we increase the counter by 1.

![[560-2.png]]
_Figure 5. Situation 1: The subarray starts from the beginning of the array._


In situation 2, the  
subarray with the target sum starts somewhere in the middle.  
That means we should add to the counter the number of times we have seen  
the prefix sum `curr_sum - target` so far: `count += h[curr_sum - target]`.

The logic is simple: the current prefix sum is `curr_sum`, and some elements  
before the prefix sum was `curr_sum - target`. All the  
elements in between sum up to `curr_sum - (curr_sum - target) = target`.

![[560-3.png]]

_Figure 6. Situation 2: The subarray starts somewhere in the middle._


# Questions

[[560. Subarray Sum Equals K]]
[[930. Binary Subarrays With Sum]]
[[437-Path-Sum-III]]


# 2d Questions

[[304. Range Sum Query 2D - Immutable]]



# Prefix Product

[[1352. Product of the Last K Numbers]]