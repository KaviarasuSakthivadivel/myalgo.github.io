# 151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

    ```Example 1:

    Input: s = "the sky is blue"
    Output: "blue is sky the"
    ```

## Solution

### 1. Reverse the Whole String and Then Reverse Each Word: ![gras](/images/leetcode/151.png)

```java
class Solution {
  public StringBuilder trimSpaces(String s) {
    int left = 0, right = s.length() - 1;
    // remove leading spaces
    while (left <= right && s.charAt(left) == ' ') ++left;

    // remove trailing spaces
    while (left <= right && s.charAt(right) == ' ') --right;

    // reduce multiple spaces to single one
    StringBuilder sb = new StringBuilder();
    while (left <= right) {
      char c = s.charAt(left);

      if (c != ' ') sb.append(c);
      else if (sb.charAt(sb.length() - 1) != ' ') sb.append(c);

      ++left;
    }
    return sb;
  }

  public void reverse(StringBuilder sb, int left, int right) {
    while (left < right) {
      char tmp = sb.charAt(left);
      sb.setCharAt(left++, sb.charAt(right));
      sb.setCharAt(right--, tmp);
    }
  }

  public void reverseEachWord(StringBuilder sb) {
    int n = sb.length();
    int start = 0, end = 0;

    while (start < n) {
      // go to the end of the word
      while (end < n && sb.charAt(end) != ' ') ++end;
      // reverse the word
      reverse(sb, start, end - 1);
      // move to the next word
      start = end + 1;
      ++end;
    }
  }

  public String reverseWords(String s) {
    // converst string to string builder 
    // and trim spaces at the same time
    StringBuilder sb = trimSpaces(s);

    // reverse the whole string
    reverse(sb, 0, sb.length() - 1);

    // reverse each word
    reverseEachWord(sb);

    return sb.toString();
  }
}
```

### 2. Deque of Words

```java
class Solution {
  public String reverseWords(String s) {
    int left = 0, right = s.length() - 1;
    // remove leading spaces
    while (left <= right && s.charAt(left) == ' ') ++left;

    // remove trailing spaces
    while (left <= right && s.charAt(right) == ' ') --right;

    Deque<String> d = new ArrayDeque();
    StringBuilder word = new StringBuilder();
    // push word by word in front of deque
    while (left <= right) {
      char c = s.charAt(left);

      if ((word.length() != 0) && (c == ' ')) {
        d.offerFirst(word.toString());
        word.setLength(0);
      } else if (c != ' ') {
        word.append(c);
      }
      ++left;
    }
    d.offerFirst(word.toString());

    return String.join(" ", d);
  }
}
```