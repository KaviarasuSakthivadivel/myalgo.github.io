## Subsequences

```java
public class SubsequencesExample {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                // Access subsequence from index i to j
                for (int k = i; k <= j; k++) {
                    System.out.print(arr[k] + " ");
                }
                System.out.println();
            }
        }
    }
}
```

In this example, we have an array `{1, 2, 3, 4}`. The nested for loops iterate through all possible subsequences, including adjacent elements. The outer loop `i` represents the starting index of the subsequence, and the inner loop `j` represents the ending index of the subsequence. The third loop `k` is used to print the subsequence elements from index `i` to `j`.

The output of the above code will be:

```java
1
1 2
1 2 3
1 2 3 4
2
2 3
2 3 4
3
3 4
4
```

Each line represents a subsequence of the original array.

## Finding first decreasing element from the right

In this case as well, we consider the given number n as a character array a.  
First, we observe that for any given sequence that is in descending order, no next larger permutation is possible.  
For example, no next permutation is possible for the following array:

```csharp
[9, 5, 4, 3, 1]
```

We need to find the first pair of two successive numbers a[i] and a[i−1], from the right, which satisfy  
a[i]>a[i−1]. Now, no rearrangements to the right of a[i−1] can create a larger permutation since that subarray consists of numbers in descending order.  
Thus, we need to rearrange the numbers to the right of a[i−1] including itself.

Now, what kind of rearrangement will produce the next larger number? We want to create the permutation just larger than the current one. Therefore, we need to replace the number a[i−1] with the number which is just larger than itself among the numbers lying to its right section, say ![[31_nums_graph.png]]a[j].



We swap the numbers a[i−1] and a[j]. We now have the correct number at index i−1. But still the current permutation isn't the permutation  
that we are looking for. We need the smallest permutation that can be formed by using the numbers only to the right of a[i−1]. Therefore, we need to place those  
numbers in ascending order to get their smallest permutation.

But, recall that while scanning the numbers from the right, we simply kept decrementing the index  
until we found the pair a[i] and a[i−1] where, a[i]>a[i−1]. Thus, all numbers to the right of a[i−1] were already sorted in descending order.  
Furthermore, swapping a[i−1] and a[j] didn't change that order.  
Therefore, we simply need to reverse the numbers following a[i−1] to get the next smallest lexicographic permutation.

```java
class Solution {
    public int nextGreaterElement(int n) {
        char[] numArr = ("" + n).toCharArray();

        int i = numArr.length - 2;
        while(i >= 0 && numArr[i + 1] <= numArr[i]) {
            i--;
        }

        if(i < 0) { // decreasing numbers, no greater element!
            return -1;
        }

        int j = numArr.length - 1;

        while(j >= 0 && numArr[j] <= numArr[i]) {
            j--;
        }

        swap(numArr, i, j);
        reverse(numArr, i + 1);

        try {
            return Integer.parseInt(new String(numArr));
        } catch(Exception e) {
            return -1;
        }
    }

    private void reverse(char[] a, int start) {
        int end = a.length - 1;
        while(start < end) {
            swap(a, start, end);
            start++;
            end--;
        }
    }

    private void swap(char[] a, int i, int j) {
        char temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}
```

## Subarray ranges in 1d array

[[2104. Sum of Subarray Ranges]]

```java
public long subArrayRanges(int[] nums) {
	int n = nums.length;
	long answer = 0;
	for(int left = 0; left < n; left++) {
		for(int right = left; right < n; right++) {

			int minVal = Integer.MAX_VALUE, maxVal = Integer.MIN_VALUE;
			
			for(int i = left; i <= right; i++) {
				minVal = Math.min(minVal, nums[i]);
				maxVal = Math.max(maxVal, nums[i]);
			}

			answer += (long)(maxVal - minVal);
		}
	}

	return answer;
}
```

