# 276. Paint Fence
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

### Thoughts

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

|       |    post1  |post2  |post3  |    
| ----- |     ----- | ----- | ----- |      
|  1    |     c1    | c1    | c2    |
|  2    |     c1    | c2    | c1    |
|  3    |     c1    | c2    | c2    |
|  4    |     c2    | c1    | c1    | 
|  5    |     c2    | c1    | c2    |
|  6    |     c2    | c2    | c1    |

There are three cases we need to consider here, 

When `k=1`, there are K choices to choose from.

When `k=2` **(Same color)**, there are K * 1 choices to choose from. For the first fence, we have K choices, for the second, we need to choose the same color, so multiply by 1. 

When `k=2` **(Different color)**, there are K * (K - 1) choices. First the first fence, we have K choices, for the second, we have one minus. So, `same` + `different` is the total no of ways we can paint the fence. 

	So, (k + (k * k - 1)) will be the total number of ways to paint, when k = 2. 
 
When `k=3` **(Same color)** For the first two fence, we don't know whether it is painted same or different. 

<u>There are two possibilities</u>

1. 1st two are same, means we have only `k-1` choices for the third fence. So, `same * (k - 1)`
2. 1st two are different, means we have k - 1 choices here as well. 

**So, different = (same * (k - 1)) + (different * (k - 1))**

Video: [Youtube](https://www.youtube.com/watch?v=deh7UpSRaEY&t=16s&ab_channel=MissWright)

### Solution
```java
public class PaintFence {
    public static int numWaysPaintFence(int n, int k) {
        if( n == 0 || k == 0) {
            return 0;
        }
        if(n == 1) {
            return k;
        }
        // when k = 2 case
        int same = k;
        int different = (k * (k - 1));

        for(int i = 3; i <= n; i++) {
            int prevDifferent = different;
            different = (same + different) * (k - 1);
            same = prevDifferent;
        }
        return same + different;
    }

    public static void main(String[] args) {
        System.out.println(numWaysPaintFence(3,  2));
    }
}
```

Another approach. 


```java
public class Solution {
    public int numWays(int n, int k) {
        
        int dp[] = {0, k, k*k, 0};
        if(n <=2) return dp[n];
        for(int i =2 ;i < n;i++){
            dp[3] = dp[2] * (k-1)  + dp[1] * (k-1);
            dp[1] = dp[2];
            dp[2] = dp[3];
        }
        
        return dp[3];
    }
}
```
