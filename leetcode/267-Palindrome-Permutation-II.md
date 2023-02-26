# 267.Palindrome Permutation II
Given a strings, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Givens = "aabb", return["abba", "baab"].

Givens = "abc", return[].

### Thoughts
Take an example, "aba" odd <= 1. "abba" odd == 0

**Step1:** Get character frequency. If the odd character count is greater than 1, then impossible to generate permutations. 

**Step2:** Generate the string by backtracking. 
1. Add odd character first if the `oddCount` is greater than 0.
2. Odd even character from the beginning and end during the recursion call. 

### Solution
```java
import java.util.ArrayList;
import java.util.List;

public class PalindromePermutation {
    public static List<String> getPalindromicPermutations(String S) {
        List<String> result = new ArrayList<>();
        int[] map = new int[256];
        int oddCount = 0;
        for(char ch : S.toCharArray()) {
            map[ch]++;
            if(map[ch] % 2 == 1) {
                oddCount++;
            } else {
                oddCount--;
            }
        }
        if(S.length() == 0 || oddCount > 1) {
            return result;
        }
        String temp = "";
        // Finding the odd character from the map
        for(int i = 0; i < 256 && oddCount > 0 ; i++) {
            if(map[i] % 2 == 1) {
                temp += (char) i;
                break;
            }
        }
        backTrackHelper(result, temp, map, S.length());
        return result;

    }

    private static void backTrackHelper(List<String> result, String temp, int[] map, int n) {
        if(temp.length() == n) {
            result.add(temp);
            return;
        }
        for(int i = 0; i < 256; i++) {
            if(map[i] > 0) {
                map[i] -= 2;
                backTrackHelper(result, (char) i + temp + (char) i, map, n);
                map[i] += 2;
            }
        }
    }

    public static void main(String[] args) {
        System.out.println(getPalindromicPermutations("aabb"));
    }
}
```