An employee has to work exactly as many hours as they are told to each week. scheduling no more than a given daily maximum number of hours. On some days, the number of hours worked will be given. The employee gets to choose the remainder of their schedule, within the given limits. 

A completed schedule consists of exactly 7 digits in the range 0 to 8 that represent each day's hours to be worked. A pattern string similar to the schedule will be given, but with some of the digits replaced by a question mark, ?, (ascii 63 decimal). Given a maximum number of hours that can be worked in a day, replace the question marks with digits so that the sum of the scheduled hours is exactly the hours that must be worked in a week.

Example pattern = '08??840' work_ hours = 24 day_hours = 4 There are two days on which they must work 24 - 20 = 4 more hours for the week.




```java
import java.util.LinkedList;
import java.util.List;

public class WorkSchedule {

    private static List<String> findSchedules(String pattern, int workHours, int dayHours) {
        List<String> workScheduleList = new LinkedList<>();
        int noOfQuestionMark = 0, totalWorkedHours = 0;

        for(char ch : pattern.toCharArray()) {
            if(ch == '?') {
                noOfQuestionMark++;
            } else {
                totalWorkedHours += (ch - '0');
            }
        }

        int deficitHours = workHours - totalWorkedHours;

        fillSchedules(pattern.toCharArray(), dayHours, 0, deficitHours, noOfQuestionMark, workScheduleList);
        return workScheduleList;
    }

    // Backtracking function
    private static void fillSchedules(char[] pattern, int actualDayHours, int index, int deficitHours, int remainingQuestionMark, List<String> workScheduleList) {
        if(deficitHours < 0 || remainingQuestionMark < 0) {
            return;
        }

        if(pattern.length == index) {
            if(deficitHours == 0 && remainingQuestionMark == 0) {
                workScheduleList.add(String.valueOf(pattern));
            }
            return;
        }

        if(pattern[index] == '?') {
            for(int i = 0; i <= actualDayHours; i++) {
                pattern[index] = (char) (i + '0');
                fillSchedules(pattern, actualDayHours, index + 1, deficitHours - i, remainingQuestionMark - 1, workScheduleList);
                pattern[index] = '?';
            }
        } else {
            fillSchedules(pattern, actualDayHours, index + 1, deficitHours, remainingQuestionMark, workScheduleList);
        }
    }

    public static void main(String[] args) {
        String pattern = "08??840";
        int workHours = 24;
        int dayHours = 4;
        System.out.println(findSchedules(pattern, workHours, dayHours));

        pattern = "????8??";
        workHours = 56;
        dayHours = 8;
        System.out.println(findSchedules(pattern, workHours, dayHours));
    }
}

```