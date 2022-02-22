# 171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

    For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

    Example 1:

    Input: columnTitle = "A"
    Output: 1
    Example 2:

    Input: columnTitle = "AB"
    Output: 28
    Example 3:

    Input: columnTitle = "ZY"
    Output: 701

### Solution

    This problem can be solved as if it is a problem of converting base-26 number system to base-10 number system.

Intuition


### Approach 1: Right to Left
Let's tabulate the titles of an excel sheet in a table. There will be 26 rows in each column. Each cell in the table represents an excel sheet title.

An image: ![gras](/images/leetcode/171.png)


Pay attention to the "1 green block", "1 orange block" and "1 blue block" in the figure. These tell how bigger blocks are composed of smaller blocks. For example, blocks of 2-character titles are composed of 1-character blocks and blocks of 3-character titles are composed of 2-character blocks. This information is useful for finding a general pattern when calculating the values of titles.

Let's say we want to get the value of title AZZC. This can be broken down as 'A***' + 'Z**' + 'Z*' + 'C'. Here, the *s represent smaller blocks. * means a block of 1-character titles. ** means a block of 2-character titles. There are 261 titles in a block of 1-character titles. There are 262 titles in a block of 2-character titles.

    Scanning AZZC from right to left while accumulating results:

    First, ask the question, what the value of 'C' is:
    'C' = 3 x 260 = 3 x 1 = 3
    result = 0 + 3 = 3
    Then, ask the question, what the value of 'Z*' is:
    'Z*' = 26 x 261 = 26 x 26 = 676
    result = 3 + 676 = 679
    Then, ask the question, what the value of 'Z**' is:
    'Z**' = 26 x 262 = 26 x 676 = 17576
    result = 679 + 17576 = 18255
    Finally, ask the question, what the value of 'A***' is:
    'A***' = 1 x 263 = 1 x 17576 = 17576
    result = 18255 + 17576 = 35831

### Algorithm

1. To get indices of alphabets, create a mapping of alphabets and their corresponding values. (1-indexed)
2. Initialize an accumulator variable result.
3. Starting from right to left, calculate the value of the character associated with its position and add it to result.


```java
class Solution {
    public int titleToNumber(String columnTitle) {
        HashMap<Character, Integer> map = new HashMap<>();
        
        for(int i = 0; i < 26; i++) {
            int ch = i + 65;
            map.put((char) ch, i + 1);
        }
        
        int n = columnTitle.length();
        int result = 0;
        int i = 0;
        while(i < n) {
            result += (map.get(columnTitle.charAt(n - 1 - i)) * Math.pow(26, i));
            i++;
        }
        
        return result;
    }
}
```

### Aproach 2

Rather than scanning from right to left as described in Approach 1, we can also scan the title from left to right.

For example, if we want to get the decimal value of string "1337", we can iteratively find the result by scanning the string from left to right as follows:

    '1' = 1
    '13' = (1 x 10) + 3 = 13
    '133' = (13 x 10) + 3 = 133
    '1337' = (133 x 10) + 7 = 1337
    Instead of base-10, we are dealing with base-26 number system. Based on the same idea, we can just replace 10s with 26s and convert alphabets to numbers.

For a title "LEET":

    L = 12
    E = (12 x 26) + 5 = 317
    E = (317 x 26) + 5 = 8247
    T = (8247 x 26) + 20 = 214442

In Approach 1, we have built a mapping of alphabets to numbers. There is another way to get the number value of a character without building an alphabet mapping. You can do this by converting a character to its ASCII value and subtracting ASCII value of character 'A' from that value. By doing so, you will get results from 0 (for A) to 25 (for Z). Since we are indexing from 1, we can just add 1 up to the result. This eliminates a loop where you create an alphabet to number mapping which was done in Approach 1.

```java
class Solution {
    public int titleToNumber(String s) {
        int result = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            result = result * 26;
            // In Java, subtracting characters is subtracting ASCII values of characters
            result += (s.charAt(i) - 'A' + 1);
        }
        return result;
    }
}
```

