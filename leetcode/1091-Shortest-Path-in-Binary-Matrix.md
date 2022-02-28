# 1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

    Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4

![gras](/images/leetcode/1091_1.png)


### Solution
If an interviewer asks you this question in an interview, then their goal is probably to determine that:

You can recognize that this is a typical shortest path problem that can be solved with a Breadth-first search (BFS).
You can correctly implement a BFS to solve it.
For bonus points, you know that the solution could be optimized using the A* algorithm.

![gras](/images/leetcode/1091_2.png)

```directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]```

### BFS approach without overwriting the input

```java
class Solution {
    private int[][] directions = new int[][]{
        {1, -1}, {1, 0}, {1, 1}, {0, -1}, {0, 1}, {-1, -1}, {-1, 0}, {-1, 1}
    };
    public int shortestPathBinaryMatrix(int[][] grid) {
        // Base cases when the cell(0, 0) and cell(n, m) are 1
        
        if(grid[0][0] == 1 || grid[grid.length - 1][grid[0].length - 1] == 1) {
            return -1;
        }
        
        Queue<int[]> queue = new LinkedList<>();
        
        // row, col, distance
        queue.offer(new int[]{0, 0, 1});
        
        // boolean visited arr, so that loop is not infinite
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        visited[0][0] = true;
        
        while(!queue.isEmpty()) {
            int[] cell = queue.poll();
            
            int row = cell[0];
            int col = cell[1];
            int distance = cell[2];
            
            // if reached the end, return the distance
            if(row == grid.length - 1 && col == grid[0].length - 1) {
                return distance;
            }
            
            for(int[] neighbour : getNeighbours(grid, row, col)) {
                int neighbourRow = neighbour[0];
                int neighbourCol = neighbour[1];
                
                if(visited[neighbourRow][neighbourCol]) {
                   continue; 
                }
                
                visited[neighbourRow][neighbourCol] = true;
                queue.offer(new int[]{neighbourRow, neighbourCol, distance +
 1});
            }
        }
        return -1;
    }
    
    private List<int[]> getNeighbours(int[][] grid, int row, int col) {
        List<int[]> neighbours = new ArrayList<>();
        
        for(int[] d : directions) {
            int newRow = row + d[0];
            int newCol = col + d[1];
            
            if(newRow < 0 || newCol < 0 || newRow >= grid.length || newCol >= grid[0].length || grid[newRow][newCol] != 0) {
                continue;
            }
            neighbours.add(new int[]{newRow, newCol});
        }     
        return neighbours;
    }
}
```
