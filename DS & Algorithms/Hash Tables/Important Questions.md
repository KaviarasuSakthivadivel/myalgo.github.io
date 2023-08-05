
# Leetcode
1. [[1218. Longest Arithmetic Subsequence of Given Difference]]
2. [[1282. Group the People Given the Group Size They Belong To]]
3. [[1010. Pairs of Songs With Total Durations Divisible by 60]]
4. [[1366. Rank Teams by Votes]]
5. [[36. Valid Sudoku]]
6. 


# Interview Pen Questions

# **Nearest Repeated Entries**
---

Given an array of string, return the distance between the nearest repeated strings. If no entry is repeated, return `-1`.

**Input-Output**

**Example 1**

```javascript
Input:
[
  "This",
  "is",
  "a",
  "sentence",
  "with",
  "is",
  "repeated",
  "then",
  "repeated"
]
Output: 2
Explanation: "repeated" (index 6) and "repeated" (index 8) are 2 positions away.
```

**Example 2**

```javascript
Input:
[
  "This",
  "is",
  "a"
]
Output: -1
Explanation: There are no repeated entries.
```

```java

public static int nearestRepeatedEntries(String[] sentence) {
    HashMap<String, Integer> wordIndexMap = new HashMap<>();
    int nearestDistance = Integer.MAX_VALUE;

    for(int i = 0; i < sentence.length; i++) {
        String word = sentence[i];

        if(wordIndexMap.containsKey(word)) {
            nearestDistance = Math.min((i - wordIndexMap.get(word)), nearestDistance);
        }
        wordIndexMap.put(word, i);
    }

    return nearestDistance == Integer.MAX_VALUE ? -1 : nearestDistance;
}
```



# 532. K-diff Pairs in an Array
---

Given an array of integers `nums` and an integer `k`, return _the number of **unique** k-diff pairs in the array_.

A **k-diff** pair is an integer pair `(nums[i], nums[j])`, where the following are true:

- `0 <= i, j < nums.length`
- `i != j`
- `|nums[i] - nums[j]| == k`

**Notice** that `|val|` denotes the absolute value of `val`.

**Example 1:**

**Input:** nums = [3,1,4,1,5], k = 2
**Output:** 2
**Explanation:** There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of **unique** pairs.

**Example 2:**

**Input:** nums = [1,2,3,4,5], k = 1
**Output:** 4
**Explanation:** There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

```java
class Solution {
    public int findPairsNaive(int[] nums, int k) {
        // Naive
        int count = 0;
        
        Arrays.sort(nums);
        for(int i = 0 ; i < nums.length; i++) {
            if(i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            for(int j = i + 1; j < nums.length; j++) {
                if(j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }
                if(Math.abs(nums[j] - nums[i]) == k) {
                    count++;
                }
            }
        }
        
        
        return count;
    }
    
    public int findPairs(int[] nums, int k) {
        int count = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int i = 0 ; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        
        // If the hash map contains key + k, increment count. 
        // Special case for K = 0, where we need to check the key's value occucing twice. 
        for(int key : map.keySet()) {
            if((k > 0 && map.containsKey(key + k)) || (k == 0 && map.get(key) > 1)) {
                count++;
            }
        }
        return count;
    }
}
```


# **Minimum Time Difference**
---

Given an array of time strings (formatted as `HH:mm`), return the smallest difference between any two times in minutes.

**Input-Output**

**Example 1**

```javascript
Input: ["00:04", "23:58", "12:03"]
Output: 6
Input: The closest 2 times are "00:04" and "23:58" (by wrap-around), and they differ by 6 minutes.
```

#### Thoughts

1. Convert the time to minutes. 
2. Have a boolean array of max (60* 24) = 1440. Set true when you encounter a converted minute in the cache boolean array. Because it is duplicate case, eg. 14:00 and 14:00 in the array. 
3. Init first as MAX, last as MIN values. lowest & highest values in the array! As we iterate, do pairwise comparison! 

```java
class Solution {
    public int findMinDifference(List<String> timePoints) {
        int maxTimeSlot = 60 * 24; // 1440
        boolean[] timeCache = new boolean[maxTimeSlot];

        for(String time : timePoints) {
            int minutes = convertToMinutes(time);
            if(timeCache[minutes]) {
                return 0;
            }
            timeCache[minutes] = true;
        }


        int first = Integer.MAX_VALUE, last = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE, prev = 0;

        for(int i = 0; i < maxTimeSlot; i++) {
            if(timeCache[i]) {
                if(first != Integer.MAX_VALUE) {
                    min = Math.min(min, i - prev);
                }

                first = Math.min(first, i);
                last = Math.max(last, i);
                prev = i;
            }
        }

        return Math.min(min, first + maxTimeSlot - last);
    }

    private int convertToMinutes(String time) {
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }
}
```