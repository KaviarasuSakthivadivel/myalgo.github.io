# 186. Reverse Words in a String II
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example, Given s = "the sky is blue", return "blue is sky the".

Could you do it in-place without allocating extra space?

### Thoughts
First reverse the entire string. 

Then, for each words, split by space and reverse the words. 

### Solution

```java
import java.util.Arrays;

public class ReverseWordsII {

    private static String reverseWordsInString(char[] s) {
        reverse(s, 0, s.length - 1);

        int left = 0, right = 0;
        while(right < s.length) {
            if(s[right] == ' ') {
                reverse(s, left, right - 1);
                left = ++right;
            } else {
                right++;
            }
        }
        reverse(s, left, right - 1);

        return Arrays.toString(s);
    }

    private static void reverse(char[] arr, int start, int end) {
        int i = start;
        int j = end;
        while(i < j) {
            char temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }

    public static void main(String[] args) {
        System.out.println(reverseWordsInString("the sky is blue".toCharArray()));
    }
}
```