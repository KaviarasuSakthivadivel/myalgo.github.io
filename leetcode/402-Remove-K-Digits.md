# 402. Remove K Digits

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

    Example 1:

    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
    Example 2:

    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

## Approach
### Approach 1: Brute-force [Time Limit Exceeded]
Intuition

At the first glance, one of the first intuitions that might come to one's mind is to enumerate all the possible combinations and find the minimal number among them, i.e. brute-force.

Though after a small moment of reflection, we would easily rule it out. We could name a few reasons. The major caveat is that the algorithm would have an exponential time complexity, since we need to enumerate the combinations of selecting kk numbers out of a list of nn, i.e. C_{n}^{k}C^n_k
Even for a trial example, the algorithm could run out of the time limit.

Apart from the complexity issue, another technical issue that one needs to solve in the above brute-force approach, is to compare the values of two digit strings. As naive as it sounds, we could convert the digit string to the numerical value. Soon one would realize that this method does not scale. For an unsigned 32 bit-integer, the maximum value it can hold is a number with 10 digits (i.e. 4,294,967,295). We can expect there are plenty of test cases with strings of hundreds of digits.

One would argue that for comparison, we don't need to convert the digit string to its numeric value, but simply compare the sequence of digits one by one from left to right. Indeed, it would work.

But then, if we look at the overall problem again, it seems that there should be some deterministic way to construct the solution, without the need of exhausting all possible solutions.


### Approach 2: Greedy with Stack

Intuition

We've got a hint while entertaining the idea of brute-force, that given two sequences of digit of the same length, it is the leftmost distinct digits that determine the superior of the two numbers, e.g. for A = 1axxx, B = 1bxxx, if the digits a > b, then A > B.

With this insight, the first intuition we got for our problem is that we should iterate from the left to right, when removing the digits. The more a digit to the left-hand side, the more weight it carries.

Now that we fix on the order of the iteration, it is critical to come up some criteria on how we eliminate digits, in order to obtain the minimum value.

Let us start from a simple example. Given a sequence of digits, e.g. 425, if we are asked to remove just one digit, then from left to right, we have the candidates as 4, 2 and 5. And we compare each digit with its left neighbor. Starting from 2, which is less than its left neighbor 4. At this very moment, we are sure that we should remove the digit 4. Because the consequence of not doing so is that we won't obtain the minimum number, no matter what we do subsequently.

Imagine if we keep the digit 4, then all the possible solutions are lead with the digit 4 (i.e. 42, 45). While in one of the opposite cases, e.g. removing 4 and keeping 2, we have solutions lead with 2 (i.e. 25), which is obviously less than any of the solutions of keeping the digit 4.


### Solution
```java
class Solution {
    public String removeKdigits(String num, int k) {
        LinkedList<Character> stack = new LinkedList<>();
        
        for(char digit : num.toCharArray()) {
            while(!stack.isEmpty() && k > 0 && stack.peekLast() > digit) {
                stack.removeLast();
                k--;
            }
            stack.addLast(digit);
        }
        
        while(k > 0) {
            stack.removeLast();
            k--;
        }
        
        StringBuilder sb = new StringBuilder();
        
        // Remove only the leading zero
        boolean hasLeadingZero = true;
        for(char digit : stack) {
            if(hasLeadingZero && digit == '0') {
                continue;
            }
            
            hasLeadingZero = false;
            sb.append(digit);
        }
        
        return sb.length() > 0 ? sb.toString() : "0";
    }
}
```
