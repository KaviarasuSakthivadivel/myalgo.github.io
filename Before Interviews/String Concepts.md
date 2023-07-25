## Check if subsequence

```java
class Solution {
    public int numMatchingSubseq(String s, String[] words) {
        int count = 0;

        for(String word : words) {
            if(isSubsequence(s, word)) {
                count++;
            }
        }

        return count;
    }

    private boolean isSubsequence(String word, String pattern) {
        char[] wordArr = word.toCharArray();
        char[] patternArr = pattern.toCharArray();
        int idx = 0;
        for(char ch : wordArr) {
            if(idx < patternArr.length && ch == patternArr[idx]) {
                idx++;
            }
        }
        return (idx == patternArr.length);
    }
}
```

