# 1064. Fixed Point

Given an array of distinct integers arr, where arr is sorted in ascending order, return the smallest index i that satisfies arr[i] == i. If there is no such index, return -1.

    Example 1:

    Input: arr = [-10,-5,0,3,7]
    Output: 3
    Explanation: For the given array, arr[0] = -10, arr[1] = -5, arr[2] = 0, arr[3] = 3, thus the output is 3.

### Solution

In this problem, the length of the array can be at max 10^410 4. In most cases, we can solve a problem involving \leq≤ 10^810 8
operations with an O(N)O(N) time complexity solution. A simple linear search solution with O(N)O(N) time and O(1)O(1) space complexity would be enough to pass the test cases. But most probably this solution would invite a follow-up, asking to do better. Hence, we will discuss a better-optimized solution than linear search in this article.

### Approach 1: Binary Search
Intuition

Remember that the array we are given is sorted in ascending order. Whenever you are working with sorted data, it is always worth considering whether binary search can be applied to the current problem. Hence, let's see if we can use binary search to solve this problem more efficiently.


Generally, a binary search solution has the following steps:

1. Define the search boundary for the answer variable, say [left, right]. This range defines the possible values of the answer to the problem.

2. Find the midpoint of the above range; here, we will define the midpoint as mid = (left + right) / 2.

3. Check if midmid can be the answer to our problem.

4. Based on the above check, we redefine our search boundary. Precisely, we reduce the search space to half of the original search space.
5. We either reduce it to [left, mid - 1] or [mid + 1, right].
The method used to check if midmid can be the answer is problem-dependent. We will discuss this in the latter part of the article.
When mid could be the answer, then setanswerequal tomid. When the size of the search space is reduced to0i.e.,left > right, we can stop the process and return the current value ofanswer`.

```java
class Solution {
    public int fixedPoint(int[] arr) {
        int answer = -1;
        int left = 0, right = arr.length - 1;
        
        while(left <= right) {
            int mid = left + (right - left) / 2;
            
            if(arr[mid] == mid) {
                answer = mid;
                // Continue searching on the left.
                right = mid - 1;
            } else if(arr[mid] < mid) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return answer;
    }
}
```