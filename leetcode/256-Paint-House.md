# 256. Paint House
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

    Input: int[][] costs = new int[][]{
            {17, 2, 17},
            {16, 16, 5},
            {14, 3, 19}
        };
    Output: 10 - (2 + 5 + 3)

### Thoughts
Here the idea is, if we choose a color for the first house (1st row), we can't choose the same color for the second house. The problem will get reduced to choosing between other two color for the next house and so on. 

We can just modify the given costs array, starting from house 1, (index starts at 0). Just add the minimum of other two color's cost in the column of the house. 

    costs[i][0] += Math.min(costs[i - 1][1], costs[i - 1][2]);
    costs[i][1] += Math.min(costs[i - 1][0], costs[i - 1][2]);
    costs[i][2] += Math.min(costs[i - 1][0], costs[i - 1][1]);

### Solution
```java
public class PaintHouse {
    public static int minCost(int[][] costs) {
        if(costs == null || costs.length == 0) {
            return 0;
        }

        for(int i = 1; i < costs.length; i++) {
            costs[i][0] += Math.min(costs[i - 1][1], costs[i - 1][2]);
            costs[i][1] += Math.min(costs[i - 1][0], costs[i - 1][2]);
            costs[i][2] += Math.min(costs[i - 1][0], costs[i - 1][1]);
        }

        int n = costs.length - 1;
        return Math.min(costs[n][0], Math.min(costs[n][1], costs[n][2]));
    }

    public static void main(String[] args) {
        int[][] costs = new int[][]{
            {17, 2, 17},
            {16, 16, 5},
            {14, 3, 19}
        };
        System.out.println(minCost(costs));
    }
}
```