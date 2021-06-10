# 161. One Edit Distance

Given two strings S and T, determine if they are both one edit distance apart.

One edit distance: converting word1 to word2 only needs one step. You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

    Input:  s1 = "geeks", s2 = "geek"
    Output: true
    Number of edits is 1

## Thoughts
Traverse both the strings using `i`, `j` for the first and second string respectively. Keep track of different characters using `count` variable.

1. <u>**Base case:**</u> If the absolute difference between two strings are greater than 1, return `False`
2. If the current character in both the strings are same, continue. 
3. Else If the count has become 1, and still the current Character in both strings are not equal, return `False`
    1. Here we need to check if the length of the strings. 
    2. If the first string is greater, increment `i` pointer. If the second string is greater, increment `j` pointer. 
    3. Else if the strings are equal, increment count
    4. And finally increment `count`

## Solution 
```java
public class OneEditDistance {
    public static boolean isOneEditDistance(String S, String T) {
        if(Math.abs(S.length() - T.length()) > 1) {
            return false;
        }
        int i = 0, j = 0, count = 0;
        while(i < S.length() && j < T.length()) {
            if(S.charAt(i) == T.charAt(j)) {
                i++;
                j++;
            } else {
                if(count == 1) {
                    return false;
                }
                if(S.length() > T.length()) {
                    i++;
                } else if(T.length() > S.length()) {
                    j++;
                } else { // if the length of both strings are the same
                    i++;
                    j++;
                }
                count++;
            }
        }
        if(i < S.length() || j < T.length()) {
            count++;
        }

        return count == 1;
    }

    public static void main(String[] args) {
        System.out.println(isOneEditDistance("geeks", "geek"));
    }
}
````