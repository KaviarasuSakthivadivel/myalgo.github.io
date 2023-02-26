# 254. Factor Combinations

    Numbers can be regarded as product of its factors. For example,

    8 = 2 x 2 x 2;
    = 2 x 4.

    Write a function that takes an integer n and return all possible combinations of its factors.

    Note: 
    You may assume that n is always positive.
    Factors should be greater than 1 and less than n.

    Examples: 
    input: 1
    output: 
    []
    input: 37
    output: 
    []
    input: 12
    output:
    [
        [2, 6],
        [2, 2, 3],
        [3, 4]
    ]  
    input: 32
    output:
    [
    [2, 16],
    [2, 2, 8],
    [2, 2, 2, 4],
    [2, 2, 2, 2, 2],
    [2, 4, 4],
    [4, 8]
    ]

### Thoughts 
We can use backtracking to solve this problem, 


### Solution
```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class FactorCombination {
    public static List<List<Integer>> getFactors(int n) {
        List<List<Integer>> result = new ArrayList<>();
        process(2, n, result, new LinkedList<>());
        return result;
    }

    private static void process(int start, int n, List<List<Integer>> result, List<Integer> currentList) {
        if(n == 1) { // All the numbers are explored, just add current list to result
            if(currentList.size() > 1) {
                result.add(new LinkedList<>(currentList));
            }
        }

        for(int i = start; i <= n ; i++) {
            if(n % i == 0) {
                currentList.add(i);
                process(i, n / i, result, currentList);
                currentList.remove(currentList.size() - 1);
            }
        }
    }

    public static void main(String[] args) {
        System.out.println(getFactors(32));
    }
}
```
