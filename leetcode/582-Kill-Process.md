# 582. Kill Process
Given `n` processes, each process has a unique `PID (process id)` and its `PPID (parent process id)`.
Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.
We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.
Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.
Input:

pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5

Output:
 [5,10]

Explanation:

           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.

### Solution
```java
import java.util.*;

public class KillProcess {

    public static List<Integer> killProcess(int[] pid, int[] ppid, int kill) {
        List<Integer> result = new ArrayList<>();
        int size = pid.length;

        HashMap<Integer, List<Integer>> parentChildMap = new HashMap<>();
        for(int i = 0 ; i < size; i++) {
            int childPid = pid[i];
            int parentId = ppid[i];
            if(!parentChildMap.containsKey(parentId)) {
                parentChildMap.put(parentId, new ArrayList<>());
            }
            parentChildMap.get(parentId).add(childPid);
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.add(kill);
        while(!queue.isEmpty()) {
            int killedPid = queue.poll();
            result.add(killedPid);
            if(parentChildMap.containsKey(killedPid)) {
                queue.addAll(parentChildMap.get(killedPid));
            }
        }

        return result;
    }
    public static void main(String[] args) {
        int[] pid = new int[]{1, 3, 10, 5};
        int[] ppid = new int[]{3, 0, 5, 3};
        System.out.println(killProcess(pid, ppid, 5));
    }
}
```