# 277. Find the Celebrity

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

### Thoughts
Push all the guest index into the stack. Use the given arr to check for the last two elements in the stack knows or not till the stack size becomes one. 

### Solution
```java
import java.util.Stack;
import java.util.stream.IntStream;

public class CelebrityProblem {
    private static int getId(int[][] arr, int n) {
        Stack<Integer> stack = new Stack<>();
        IntStream.rangeClosed(0, n - 1).forEach(stack::add);
        while(stack.size() > 1) {
            int a = stack.pop();
            int b = stack.pop();
            if(arr[a][b] == 0) {
                stack.push(a);
            } else {
                stack.push(b);
            }
        }
        int peak = stack.pop();
        boolean found = true;

        for(int i = 0; i < n; i++) {
            if(i == peak) continue;
            if (arr[i][peak] == 0 || arr[peak][i] == 1) {
                found = false;
                break;
            }
        }
        if(!found) {
            return -1;
        }
        return peak;
    }

    public static void main(String[] args) {
        int[][] arr = new int[][]{{0, 1, 0}, {0, 0, 0}, {0, 1, 0}};
        System.out.println(getId(arr, 3));
    }
}
```