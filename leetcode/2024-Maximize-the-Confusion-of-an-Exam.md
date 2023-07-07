A teacher is writing a test with `n` true/false questions, with `'T'` denoting true and `'F'` denoting false. He wants to confuse the students by **maximizing** the number of **consecutive** questions with the **same** answer (multiple trues or multiple falses in a row).

You are given a string `answerKey`, where `answerKey[i]` is the original answer to the `ith` question. In addition, you are given an integer `k`, the maximum number of times you may perform the following operation:

- Change the answer key for any question to `'T'` or `'F'` (i.e., set `answerKey[i]` to `'T'` or `'F'`).

Return _the **maximum** number of consecutive_ `'T'`s or `'F'`s _in the answer key after performing the operation at most_ `k` _times_.

**Example 1:**

**Input:** answerKey = "TTFF", k = 2
**Output:** 4
**Explanation:** We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.

**Example 2:**

**Input:** answerKey = "TFFT", k = 1
**Output:** 3
**Explanation:** We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.

**Example 3:**

**Input:** answerKey = "TTFTTFTT", k = 1
**Output:** 5
**Explanation:** We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.


#### Solution

![[2024.png]]

#### Algorithm

1. Use a hash map `count` to record the count of `T` and `F` in the current window.
2. Set `left = 0` and `max_size = 0`, iterate `right` from `0` to `n - 1`, at each step `right`, increment `answerKey[right]` by 1:
    - Increment `count[answerKey[right]]` by 1.
        
    - While `min(count['T'], count['F']) > k`, decrement `count[answerKey[left]]` by 1 and increment `left` by 1.
        
    - Now the window is valid, update the maximum size of valid window as `max_size = max(max_size, right - left + 1)`.
        
3. Return `max_size` when the iteration ends.

```java
class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        // Sliding window solution

        HashMap<Character, Integer> charFreqMap = new HashMap<>();

        int n = answerKey.length();
        int minLength = k;

        for(int i = 0; i < k; i++) {
            Character ch = answerKey.charAt(i);
            charFreqMap.put(ch, charFreqMap.getOrDefault(ch, 0) + 1);
        }

        int left = 0;
        for(int right = k; right < n; right++) {
            Character rightCh = answerKey.charAt(right);
            charFreqMap.put(rightCh, charFreqMap.getOrDefault(rightCh, 0) + 1);

            while(Math.min(charFreqMap.getOrDefault('T', 0), charFreqMap.getOrDefault('F', 0)) > k) {
                Character leftCh = answerKey.charAt(left++);
                charFreqMap.put(leftCh, charFreqMap.get(leftCh) - 1);
            }

            minLength = Math.max(minLength, right - left + 1);
        }

        return minLength;
    }
}
```


