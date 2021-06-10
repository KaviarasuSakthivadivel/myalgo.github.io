# 170. Two Sum III - Data structure design

Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

`TwoSum()` Initializes the `TwoSum` object, with an empty array initially.

`void add(int number)` Adds number to the data structure.

`boolean find(int value)` Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
    
    EXAMPLE 1:
    Input
    ["TwoSum", "add", "add", "add", "find", "find"]
    [[], [1], [3], [5], [4], [7]]
    Output
    [null, null, null, null, true, false]

    Explanation
    TwoSum twoSum = new TwoSum();
    twoSum.add(1);   // [] --> [1]
    twoSum.add(3);   // [1] --> [1,3]
    twoSum.add(5);   // [1,3] --> [1,3,5]
    twoSum.find(4);  // 1 + 3 = 4, return true
    twoSum.find(7);  // No two integers sum up to 7, return false

## Thoughts
We can use the HashMap to store the numbers. To find a pair with a given sum, iterate through the key set of HashMap, calculate the complement `(value - currentEl)` and check whether it's present or not.

## Solution

```java
import java.util.HashMap;

public class TwoSumIII {
    HashMap<Integer, Integer> map;

    public TwoSumIII() {
        map = new HashMap<>();
    }

    public void add(int value) {
        map.put(value, map.getOrDefault(value, 0) + 1);
    }

    public boolean find(int value) {
        for(int i : map.keySet()) {
            int target = value - i;
            if(map.containsKey(target)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        TwoSumIII twoSumIII = new TwoSumIII();
        twoSumIII.add(1);
        twoSumIII.add(3);
        twoSumIII.add(5);

        System.out.println(twoSumIII.find(4));
        System.out.println(twoSumIII.find(7));
    }
}

```