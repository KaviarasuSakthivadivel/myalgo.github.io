# 159. Longest Substring with At Most Two Distinct Characters
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.

## Thoughts
Use dynamic Sliding window pattern. We can use HashMap to store the frequency of the character in the current window.

1. We will insert the characters from the beginning untill we have `k=2` distinct characters in the HashMap
2. If the HashMap size is greater than `k=2` then we need to shrink the window size, while shrinking if the character's frequency is 0, then remove it from the Map. 
3. At the end, we need to update the LongestSubstring as the Math of (LongestSubstring, (end - start + 1), i.e, comparing it with the window size.

## Solution
```java
package io.educative.slidingwindow;

import java.util.HashMap;

public class LongestSubstringWithKDistinct {

    public void findLongestSubstringWithKDistinct(String str, int k) {

        HashMap<Character, Integer> hashMap = new HashMap<>();
        int windowStart = 0;
        int maxLength = Integer.MIN_VALUE;
        for(int windowEnd = 0 ; windowEnd < str.length() ; windowEnd++) {
            Character currentChar = str.charAt(windowEnd);
            hashMap.put (currentChar, hashMap.getOrDefault(currentChar, 0) + 1);

            while(hashMap.size() > k) {
                Character leftChar = str.charAt(windowStart);
                hashMap.put(leftChar, hashMap.getOrDefault(leftChar, 0) - 1);
                if(hashMap.get(leftChar) == 0) {
                    hashMap.remove(leftChar);
                }
                windowStart++;
            }
            maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
        }
        System.out.println(maxLength);
    }

    public static void main(String[] args) {
        new LongestSubstringWithKDistinct().findLongestSubstringWithKDistinct("arrraacxi", 2);
    }
}
```