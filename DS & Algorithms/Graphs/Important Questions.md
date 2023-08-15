
## Water related problems

[130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)  
[200. Number of Islands](https://leetcode.com/problems/number-of-islands/)  
[694. Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/)  
[[695. Max Area of Island]]

[[1254. Number of Closed Islands]]
[[1020. Number of Enclaves]]
[[694. Number of Distinct Islands]]
[[463. Island Perimeter]]
[[417. Pacific Atlantic Water Flow]]

## BFS
[[1730. Shortest Path to Get Food]]
[[994. Rotting Oranges]]
[[1293. Shortest Path in a Grid with Obstacles Elimination]]
[[2101. Detonate the Maximum Bombs]]

## Interesting way to solve - Reverse Thinking

[[130. Surrounded Regions]]
[[[[417. Pacific Atlantic Water Flow]]]]

## River Sizes

You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size.

Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example.

Write a function that returns an array of the sizes of all rivers represented in the input matrix. The sizes don't need to be in any particular order.

### Sample Input

```
matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0],
]

```

### Sample Output

```
[1, 2, 2, 2, 5] 
```

### Hints

Since you must return the sizes of rivers, which consist of horizontally and vertically adjacent 1s in the input matrix, you must somehow keep track of groups of neighboring 1s as you traverse the matrix. Try treating the matrix as a graph, where each element in the matrix is a node in the graph with up to 4 neighboring nodes (above, below, to the left, and to the right), and traverse it using a popular graph-traversal algorithm like Depth-first Search or Breadth-first Search.

By traversing the matrix using DFS or BFS as mentioned in Hint #1, any time that you encounter a 1 you can traverse the entire river that this 1 is a part of (and keep track of its size) by simply iterating through the given node's neighboring nodes and their own neighboring nodes so long as the nodes are 1s.

Naturally, many nodes in the graph mentioned in Hint #1 will have overlapping neighboring nodes, and as you traverse the matrix, you will undoubtedly encounter nodes that you have previously visited. In order to prevent mistakenly calculating the same river's size multiple times and to avoid doing needless computational work, try keeping track of every node that you visit in an auxiliary data structure and only performing important computations on unvisited nodes. What data structure would be ideal here?

Optimal Space & Time Complexity

O(wh) time | O(wh) space - where w and h are the width and height of the input matrix

### Solution 1

```java

import java.util.List;
import java.util.ArrayList;
import java.util.Stack;

class Program {
    public static List<Integer> riverSizes(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        ArrayList<Integer> result = new ArrayList<>();
        boolean[][] visited = new boolean[n][m];
        for(int i = 0; i < matrix.length; i++) {
            for(int j = 0; j < matrix[0].length; j++) {
                if(!visited[i][j]) {
                    traverseNodes(matrix, result, i, j, visited);
                }
            }
        }
        return result;
    }
    
    private static void traverseNodes(int[][] matrix, ArrayList<Integer> result, int i, int j, boolean[][] visited) {
        Stack<Integer[]> stack = new Stack<>();
        stack.push(new Integer[]{i, j});
        int riverSize = 0;
        while(!stack.isEmpty()) {
            Integer[] top = stack.pop();
            i = top[0];
            j = top[1];
            
            if(visited[i][j]) {
                continue;
            }
            visited[i][j] = true;
            if(matrix[i][j] == 0) {
                continue;
            }
            riverSize++;
            ArrayList<Integer[]> neighbours = getNeighbours(matrix, visited, i, j);
            for(Integer[] n : neighbours) {
                stack.push(n);
            }
        }
    
        if(riverSize > 0) {
            result.add(riverSize);
        }
    }

    private static ArrayList<Integer[]> getNeighbours(int[][] matrix, boolean[][] visited, int i, int j) {
        ArrayList<Integer[]> list = new ArrayList<>();
        if(i > 0 && !visited[i - 1][j]) {
            list.add(new Integer[]{i - 1, j});
        }
        if(i < matrix.length - 1 && !visited[i + 1][j]) {
            list.add(new Integer[]{i + 1, j});
        }
        if(j > 0 && !visited[i][j - 1]) {
            list.add(new Integer[]{i, j - 1});
        }
        if(j < matrix[0].length - 1 && !visited[i][j + 1]) {
            list.add(new Integer[]{i, j + 1});
        }
        return list;
    }
}
```

### Solution 2

```java
import java.util.*;

class Program {
  public static List<Integer> riverSizes(int[][] matrix) {
    // O(n*m) time  where n is the length of matrix and m is the length of matrix[0]
    // O(n*m) space
    List<Integer> myList = new ArrayList<>();

    for(int i = 0; i < matrix.length; i++)
    {
      for(int j = 0; j < matrix[0].length; j++)
      {
        if(matrix[i][j] == 1)
          myList.add(DFS(0, i, j, matrix));
      }
    }
    return myList;
  }

  public static int DFS(int size, int i, int j, int[][] matrix) {
    if(i < 0 || i >= matrix.length || j < 0 || j >= matrix[0].length || matrix[i][j] == 0)
      return 0;

    matrix[i][j] = 0;

    int up = DFS(size, i+1, j, matrix);
    int down = DFS(size, i-1, j, matrix);
    int left = DFS(size, i, j-1, matrix);
    int right = DFS(size, i, j+1, matrix);

    size += up + down + left + right;
    size += 1;

    return size;
  }
}
```