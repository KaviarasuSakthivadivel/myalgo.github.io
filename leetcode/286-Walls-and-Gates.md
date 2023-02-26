# 286. Walls and Gates
You are given a m x n 2D grid initialized with these three possible values.

1. -1 - A wall or an obstacle. 
2. 0 - A gate. 
3. INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647. Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:

    INF  -1  0  INF
    INF INF INF  -1
    INF  -1 INF  -1
    0  -1 INF INF
After running your function, the 2D grid should be:

    3  -1   0   1
    2   2   1  -1
    1  -1   2  -1
    0  -1   3   4

### Thoughts
[Good Youtube explanation](https://www.youtube.com/watch?v=Pj9378ZsCh4)

Here start from the `gate` coordinate and start exploring all the reachable nodes from there. Update the minimum distance that can be reached from the gate node. 


### Solution

#### DFS 
```java
import java.util.Arrays;

public class WallsAndGates {

    private static void wallsAndGates(int[][] grid) {
        for(int i = 0 ; i < grid.length; i++) {
            for(int j = 0; j < grid[i].length; j++) {
                // 0 represent gate, so run dfs to fill the reachable nodes with minimum distance
                if(grid[i][j] == 0) {
                    dfs(i, j, 0, grid);
                }
            }
        }
        for(int[] arr: grid) {
            System.out.println(Arrays.toString(arr));
        }
    }

    private static void dfs(int i, int j, int distance, int[][] grid) {
        if(i < 0 || i >= grid.length || j < 0 || j >= grid[i].length || grid[i][j] < distance || grid[i][j] == -1) {
            return;
        }
        grid[i][j] = distance;

        dfs(i - 1, j, distance + 1, grid);
        dfs(i, j - 1, distance + 1, grid);
        dfs(i + 1, j, distance + 1, grid);
        dfs(i, j + 1, distance + 1, grid);
    }

    public static void main(String[] args) {
        final int INF = 2147483647;
        int[][] grid = new int[][]{{INF, -1, 0, INF}, {INF, INF, INF, -1}, {INF, -1, INF, -1}, {0, -1, INF, INF}};
        wallsAndGates(grid);
    }
}
```



### Approach #2 (Breadth-first Search) [Accepted]

Instead of searching from an empty room to the gates, how about searching the other way round? In other words, we initiate breadth-first search (BFS) from all gates at the same time. Since BFS guarantees that we search all rooms of distance d before searching rooms of distance d + 1, the distance to an empty room must be the shortest.

```java 
private static final int EMPTY = Integer.MAX_VALUE;
private static final int GATE = 0;
private static final List<int[]> DIRECTIONS = Arrays.asList(
        new int[] { 1,  0},
        new int[] {-1,  0},
        new int[] { 0,  1},
        new int[] { 0, -1}
);

public void wallsAndGates(int[][] rooms) {
    int m = rooms.length;
    if (m == 0) return;
    int n = rooms[0].length;
    Queue<int[]> q = new LinkedList<>();
    for (int row = 0; row < m; row++) {
        for (int col = 0; col < n; col++) {
            if (rooms[row][col] == GATE) {
                q.add(new int[] { row, col });
            }
        }
    }
    while (!q.isEmpty()) {
        int[] point = q.poll();
        int row = point[0];
        int col = point[1];
        for (int[] direction : DIRECTIONS) {
            int r = row + direction[0];
            int c = col + direction[1];
            if (r < 0 || c < 0 || r >= m || c >= n || rooms[r][c] != EMPTY) {
                continue;
            }
            rooms[r][c] = rooms[row][col] + 1;
            q.add(new int[] { r, c });
        }
    }
}
```