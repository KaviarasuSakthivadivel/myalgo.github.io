# 163. Missing Ranges

Given a sorted integer array **nums**, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

    Example:
    Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
    Output: ["2", "4->49", "51->74", "76->99"]

### Thoughts
Have a variable `start` assigned as lower. Then loop through the nums array as `end`. 

If the start is less than end, add range as `(start, end - 1);`
Make start as `end + 1`

Finally, if the `start` is less than `upper`, then include those range as well, ie, `(start, upper);`


### Solution

```java
import java.util.ArrayList;
import java.util.List;

public class FindMissingRange {

    public static void addRange(int lower, int upper, List<String> missingRanges) {
        if(lower == upper) {
            missingRanges.add(String.valueOf(lower));
            return;
        }
        missingRanges.add(String.format("%d->%d", lower, upper));
    }

    private static List<String> findMissingRange(int[] nums, int lower, int upper) {
        int start = lower;
        List<String> missingRanges = new ArrayList<>();
        for(int end : nums) {
            if(start < end) {
                addRange(start, end - 1, missingRanges);
            }
            start = end + 1;
        }

        if(start < upper) {
            addRange(start, upper, missingRanges);
        }
        return missingRanges;
    }

    public static void main(String[] args) {
        System.out.println(findMissingRange(new int[]{1, 3, 50, 75}, 0, 99));
    }
}
```