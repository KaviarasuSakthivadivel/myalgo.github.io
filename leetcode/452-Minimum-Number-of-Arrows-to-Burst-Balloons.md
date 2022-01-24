# 452. Minimum Number of Arrows to Burst Balloons

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

    Example 1:

    Input: points = [[10,16],[2,8],[1,6],[7,12]]
    Output: 2
    Explanation: The balloons can be burst by 2 arrows:
    - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
    - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].


### 1. Greedy: ![gras](/images/leetcode/452.png)

Let's sort the balloons by the end coordinate, and then check them one by one. The first balloon is a green one number 0, it ends at coordinate 6, and there is no balloons ending before it because of sorting.

The other balloons have two possibilities :

To have a start coordinate smaller than 6, like a red balloon. These ones could be burst together with the balloon 0 by one arrow.

To have a start coordinate larger than 6, like a yellow balloon. These ones couldn't be burst together with the balloon 0 by one arrow, and hence one needs to increase the number of arrows here.

Algorithm

    Now the algorithm is straightforward :

    Sort the balloons by end coordinate x_end.

    Initiate the end coordinate of a balloon which ends first : first_end = points[0][1].

    Initiate number of arrows: arrows = 1.

    Iterate over all balloons:

    If the balloon starts after first_end:

    Increase the number of arrows by one.

    Set first_end to be equal to the end of the current balloon.

    Return arrows.


### Solution 

```java

class Solution {
    public int findMinArrowShots(int[][] points) {
        if(points == null || points.length == 0) {
            return 0;
        }
        
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
        int firstEnd = points[0][1];
        
        int minArrows = 1;
        
        for(int[] point : points) {
            int xStart = point[0];
            int xEnd = point[1];
            
            if(xStart > firstEnd) {
                minArrows++;
                firstEnd = xEnd;
            }
        }
        
        return minArrows;
    }
}

```

### Similar problem : Erase Overlapping intervals

This method can also be applied to find the number of intervals to remove the certain intervals to make them non overlapping.
Follow the same algorithm as discussed with a small change in the p[0] >= end and also in the return statement.
givenIntervalLength - count

```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0)
            return 0;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        int count = 0;
        int end = Integer.MIN_VALUE;
        for (int [] interval: intervals) {
            if (interval[0] >= end) {
                end = interval[1];
                count += 1;
            }
        }
        return intervals.length - count;
    }
}
```