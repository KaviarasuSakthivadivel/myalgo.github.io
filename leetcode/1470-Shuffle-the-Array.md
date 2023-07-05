# 1470. Shuffle the Array

Given the array `nums` consisting of `2n` elements in the form `[x1,x2,...,xn,y1,y2,...,yn]`.

_Return the array in the form_ `[x1,y1,x2,y2,...,xn,yn]`.

**Example 1:**

**Input:** nums = [2,5,1,3,4,7], n = 3
**Output:** [2,3,5,4,1,7] 
**Explanation:** Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

**Example 2:**

**Input:** nums = [1,2,3,4,4,3,2,1], n = 4
**Output:** [1,4,2,3,3,2,4,1]

**Explanation:**
https://www.youtube.com/watch?v=IvIKD_EU8BY&ab_channel=NeetCodeIO

**Storing two numbers together:**

aaa is the first number, bbb is the second number.

We can left shift bbb by 101010 bits and take its bitwise-OR with aaa.  
When we take any bit's bitwise-OR with 000, it results in the same bit, and 111 results in 111.

The first 101010 bits in bnewb_{new}bnew​ are 000. So, when we take its bitwise-OR with aaa, the result's first 101010 bits will have aaa's 101010 bits, and the next 101010 bits of aaa are 000, so the result's next 101010 will store bbb's 101010 bits there.  
Thus the final result has bits of both aaa and bbb.

![[1470-Shuffle-the-Array-1.png]]

**Extracting both numbers:**

result\text{result}result is the number having both numbers, aaa (first number) and, bbb (second number).

result\text{result}result's first 101010 bits contain aaa. Thus, we can retrieve it by taking bitwise-AND with 0000000000 11111111110000000000 \space 11111111110000000000 1111111111 (102310231023 in decimal).  
When we take a bit's AND with 111 it results in the same bit and with 000 results in 000.

result\text{result}result's next 101010 bits contain bbb, thus we can retrieve it by right shifting it by 101010 bits.

![[1470-Shuffle-the-Array-2.png]]

```java

class Solution {
    public int[] shuffle(int[] nums, int n) {
        
        // Save the pair (x1, y1), (x2, y2) in nums[0], nums[1]..
        for(int i = 0; i < n; i++) {
            nums[i] = nums[i] << 10;
            nums[i] = nums[i] | nums[i + n];
        }

        int bitMask = (int) Math.pow(2, 10) - 1;
        int j = n * 2 - 1;
        for(int i = n - 1; i >= 0; i--) {
            int y = nums[i] & bitMask;
            int x = nums[i] >> 10;
            nums[j] = y;
            nums[j - 1] = x;
            j -= 2;
        }

        return nums;

    }

    public int[] shuffleUsingTempArray(int[] nums, int n) {
        int[] result = new int[2 * n];

        for(int i = 0; i < n; i++) {
            result[2 * i] = nums[i];
            result[2 * i + 1] = nums[n + i];
        }
        return result;
    }
}
```


