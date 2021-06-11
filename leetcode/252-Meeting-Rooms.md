# 252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,

Given [[0, 30],[5, 10],[15, 20]], return `false`.

### Solution 
```java
import java.util.Arrays;

public class MeetingRooms {
    public static boolean canAttendMeetings(Interval[] intervals) {
        if(intervals == null || intervals.length <= 1) {
            return true;
        }

        Arrays.sort(intervals, (i1, i2) -> {
            if(i1.start == i2.start) {
                return i1.end - i2.end;
            } else {
                return i1.start - i2.start;
            }
        });

        for(int i = 1 ; i < intervals.length; i++) {
            Interval current = intervals[i];
            Interval previous = intervals[i - 1];

            if(current.start < previous.end) {
                return false;
            }
        }

        return true;
    }


    public static void main(String[] args) {
        Interval[] intervals = new Interval[]{
            new Interval(0, 30),
            new Interval(5, 10),
            new Interval(15, 20)
        };

        System.out.println(canAttendMeetings(intervals));
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