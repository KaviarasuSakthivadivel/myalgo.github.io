# 9. Palindrome Number

Given an integer `x`, return `true` _if_ `x` _is a_  _**palindrome**__, and_ `false` _otherwise_.

**Example 1:**

**Input:** x = 121
**Output:** true
**Explanation:** 121 reads as 121 from left to right and from right to left.

**Example 2:**

**Input:** x = -121
**Output:** false
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

### Intuition 

https://interviewpen.com/courses/data-structures-and-algorithms/check-if-a-number-is-a-palindrome

```java
class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0) {
            return false;
        }
        int digits = (int) (Math.floor(Math.log10(x))) + 1;
        int msdMask = (int) Math.pow(10, digits - 1);

        for(int i = 0; i < digits / 2; i++) {
            int msd = x / msdMask;
            int lsd = x % 10;

            if(msd != lsd) {
                return false;
            }

            x = x % msdMask;
            x = x / 10;

            msdMask = msdMask / 100;
        }
        return true;
    }

    public boolean isPalindromeUsingReverse(int x) {
        int n = x;
        int reverse = 0;
        while(n > 0) {
            reverse = (reverse * 10) + (n % 10);
            n = n / 10;
        }
        
        // System.out.println(reverse);
        
        return (reverse == x);
    }
}
```