# Introduction
    
## Contents
* [Maximum Sum Subarray of Size K](1.md)
* [[1248. Count Number of Nice Subarrays]]
* [[2024-Maximize-the-Confusion-of-an-Exam]]

- 1358. [Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516977/JavaC++Python-Easy-and-Concise)
- 1248. [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-atMost(K)-atMost(K-1))
- 1234. [Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/discuss/408978/javacpython-sliding-window/367697)
- 1004. [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/javacpython-sliding-window/379427?page=3)
- 930. [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/discuss/186683/)
- 992. [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window)
- 904. [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/discuss/170740/Sliding-Window-for-K-Elements)
- 862. [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque)
- 209. [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/discuss/433123/JavaC++Python-Sliding-Window)

Exactly `K` times = at most `K` times - at most `K - 1` times

atMost(A, S) counts the number of the subarrays of A the sum of which is at most(less than or equal to) S. Therefore, we can use atMost(A, S) - atMost(A, S - 1) to get the number of the subarrays the sum of which is exactly S.  

In the atMost function, the i to j window represents the subarrays. We use the j pointer to expand the window, when the sum of all numbers in the window is bigger than S, it's time for us to move the i pointer to shorten the window. Through this process, we can count the number of the subarrays.