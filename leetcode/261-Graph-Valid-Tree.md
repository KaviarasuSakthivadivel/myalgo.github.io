# 261. Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

### Thoughts

A Tree is a special type of undirected graph, which satisfies the following conditions. 
1. Graph is connected. 
2. It has no cycle. 

Being connected means you can start from any node and reach any other node. To prove it, we can do either BFS or DFS, here I'm using BFS to check whether each node is visited only once. If there is a loop, you will end up visited the already seen node in the traversal. 

### Solution
```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class GraphValidTree {
    public static boolean validTree(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0 ; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] e : edges) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }

        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);

        while(!queue.isEmpty()) {
            int u = queue.poll();
            // Checking if the node is already visited, there exists a cycle, so return false
            if(visited[u]) { 
                return false;
            }
            visited[u] = true;
            for(int v : graph.get(u)) {
                if(!visited[v]) {
                    queue.add(v);
                }
            }
        }
        for(boolean b : visited){
            if(!b) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        int[][] edges = new int[][]{
            {0, 1},
            {0, 2},
            {0, 3},
            {1, 4}
        };
        System.out.println(validTree(5, edges));
    }
}
```