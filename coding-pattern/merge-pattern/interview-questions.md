# Interview Questions
### 1. Given a sorted list of already scheduled programs and a list of new programs, write an algorithm to find if the given new programs can be scheduled or not? Each program is a pair of values where 1st value is the starting time and 2nd is the execution time.


    Input: scheduled = [P1(10, 5), P2(25, 15)], newPrograms = [P3(18, 7), P4(12, 10)]
    Output: [true, false]


In this implementation, the function returns a boolean array where the i-th element indicates whether the i-th new program can be scheduled or not. The true value at the i-th index of the result array indicates that the i-th new program can be scheduled, while false indicates that the i-th new program cannot be scheduled.

```java
public static boolean[] canSchedule(int[][] scheduled, int[][] newPrograms) {
    int n = scheduled.length;
    int m = newPrograms.length;
    int endTime = scheduled[n-1][0] + scheduled[n-1][1];
    boolean[] result = new boolean[m];
    
    for (int i = 0; i < m; i++) {
        if (newPrograms[i][0] >= endTime) {
            endTime = newPrograms[i][0] + newPrograms[i][1];
            result[i] = true;
        } else {
            result[i] = false;
        }
    }
    
    return result;
}

int[][] scheduled = {{10, 5}, {25, 15}};
int[][] newPrograms = {{18, 7}, {12, 10}};
boolean[] result = canSchedule(scheduled, newPrograms);
System.out.println(Arrays.toString(result)); // Output: [true, false]

```