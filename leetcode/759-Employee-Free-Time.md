# 759. Employee Free Time

We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.


    Example 1:

    Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
    Output: [[3,4]]
    Explanation: There are a total of three employees, and all common
    free time intervals would be [-inf, 1], [3, 4], [10, inf].
    We discard any intervals that contain inf as they aren't finite.
    Example 2:

    Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
    Output: [[5,6],[7,9]]

### Solution

```java
class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        List<Interval> output = new ArrayList<>();
        int n = schedule.size();
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> Integer.compare(schedule.get(a[0]).get(a[1]).start, schedule.get(b[0]).get(b[1]).start));
        
        
        // Adding the list number and the position of the list. Initially it will 0.
        for(int i = 0; i < schedule.size(); i++) {
            queue.add(new int[]{i, 0});
        }
        
        int[] prev = queue.peek();
        while(!queue.isEmpty()) {
            int[] current = queue.poll();
            Interval prevInterval = schedule.get(prev[0]).get(prev[1]);
            Interval currentInterval = schedule.get(current[0]).get(current[1]);
            
            if(currentInterval.start > prevInterval.end) {
                output.add(new Interval(prevInterval.end, currentInterval.start));
            }
            
            if(currentInterval.end > prevInterval.end) {
                prev = current;
            }
            
            if(schedule.get(current[0]).size() > current[1] + 1) {
                queue.add(new int[]{current[0], current[1] + 1});
            }
        }
        
        return output;
    }
}
```