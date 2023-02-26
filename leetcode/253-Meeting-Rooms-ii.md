# 253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example, Given [[0, 30],[5, 10],[15, 20]], return 2.

### Thoughts
We can use the `PriorityQueue` data structure to store all the intervals which is currently happening in time. Since we are sorting the intervals by start time, based on the next interval in the list, remove all the interval which has been completed by using `current.start >= pQueue.peek().end`. Note that, PriotityQueue will be sorted by end time.

### Solution 
```java
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class MeetingRoomsII {
    public static int minMeetingRooms(Interval[] intervals) {
        if(intervals == null || intervals.length <= 1) {
            return 1;
        }

        Arrays.sort(intervals, (i1, i2) -> {
            if(i1.start == i2.start) {
                return i1.end - i2.end;
            } else {
                return i1.start - i2.start;
            }
        });

        PriorityQueue<Interval> pQueue = new PriorityQueue<>(intervals.length, Comparator.comparingInt((i) -> i.end));
        pQueue.add(intervals[0]);
        int minRooms = 1;

        for(int i = 1 ; i < intervals.length; i++) {
            Interval current = intervals[i];
            pQueue.add(current);

            while(!pQueue.isEmpty() && current.start >= pQueue.peek().end) {
                pQueue.poll();
            }
            minRooms = Math.max(minRooms, pQueue.size());
        }
        return minRooms;
    }

    public static void main(String[] args) {
        Interval[] intervals = new Interval[]{
            new Interval(0, 30),
            new Interval(5, 10),
            new Interval(15, 20)
        };
        System.out.println(minMeetingRooms(intervals));
    }

    public static class Interval {
        int start;
        int end;
        public Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}
```