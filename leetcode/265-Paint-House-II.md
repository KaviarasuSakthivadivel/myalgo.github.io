# 265 - Paint House II
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

    Input: [[1,5,3],[2,9,4]]
    Output: 5
    Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
    Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.

### Thoughts
We need to find minimum value for the value in all the iteration of the houses. 

```python
def build_houses(matrix):
    n = len(matrix)
    k = len(matrix[0])
    solution_matrix = [[0] * k]

    # Solution matrix: matrix[i][j] represents the minimum cost to build house i with color j.
    for r, row in enumerate(matrix):
        row_cost = []
        for c, val in enumerate(row):
            row_cost.append(min(solution_matrix[r][i] for i in range(k) if i != c) + val)
        solution_matrix.append(row_cost)
    return min(solution_matrix[-1])

print build_houses([[1,5,3],[2,9,4]])
```

Here, the above algorithm enumerate through all the houses and calculate the min value and update the costs array itself. This process will take O(nk^2). 

### Solution
```java
public class PaintHouseII {
    private static int getMinCost(int[][] costs) {
        if(costs == null || costs.length <= 0) {
            return 0;
        }
        int n = costs.length;
        int k = costs[0].length;
        int prevMin = 0, prevSecondMin = 0, prevIdx = -1;

        for(int row = 0; row < n; row++) {
            int currentMin = Integer.MAX_VALUE;
            int currentSecondMin = Integer.MAX_VALUE;
            int currentIdx = -1;
            for(int j = 0; j < k; j++) {
                costs[row][j] = costs[row][j] + (prevIdx == j ? prevSecondMin : prevMin);

                if(costs[row][j] < currentMin) {
                    currentSecondMin = currentMin;
                    currentMin = costs[row][j];
                    currentIdx = j;
                } else if(costs[row][j] < currentSecondMin){
                    currentSecondMin = costs[row][j];
                }
            }

            prevMin = currentMin;
            prevSecondMin = currentSecondMin;
            prevIdx = currentIdx;
        }
        return costs[n - 1][k -1];
    }

    public static void main(String[] args) {
        int[][] costs = new int[][]{{1, 5, 3}, {2, 9, 4}};
        System.out.println(getMinCost(costs));
    }
}
```