# 323. Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between a_i and b_i in the graph.

Return the number of connected components in the graph.


## Solution
### Algorithm

1. Create an adjacency list such that adj[v] contains all the adjacent vertices of vertex v.
2. Initialize a hashmap or array, visited, to track the visited vertices.
3. Define a counter variable and initialize it to zero.
4. Iterate over each vertex in edges, and if the vertex is not already in visited, start a DFS from it. Add every vertex visited during the DFS to visited.
5. Every time a new DFS starts, increment the counter variable by one.
6. At the end, the counter variable will contain the number of connected components in the undirected graph.

```java

class Solution {
    
     private void dfs(List<Integer>[] adjList, int[] visited, int startNode) {
        visited[startNode] = 1;
         
        for (int i = 0; i < adjList[startNode].size(); i++) {
            if (visited[adjList[startNode].get(i)] == 0) {
                dfs(adjList, visited, adjList[startNode].get(i));
            }
        }
    }
    
    public int countComponents(int n, int[][] edges) {
        int components = 0;
        int[] visited = new int[n];
        
        List<Integer>[] adjList = new ArrayList[n]; 
        for (int i = 0; i < n; i++) {
            adjList[i] = new ArrayList<Integer>();
        }
        
        for (int i = 0; i < edges.length; i++) {
            adjList[edges[i][0]].add(edges[i][1]);
            adjList[edges[i][1]].add(edges[i][0]);
        }
        
        for (int i = 0; i < n; i++) {
            if (visited[i] == 0) {
                components++;
                dfs(adjList, visited, i);
            }
        }
        return components;
    }
}

```


### Approach 2

Algorithm

1. Initialize a variable count with the number of vertices in the input.
2. Traverse all of the edges one by one, performing the union-find method combine on each edge. If the endpoints are already in the same set, then keep traversing. If they are not, then decrement count by 1.
3. After traversing all of the edges, the variable count will contain the number of components in the graph.

```java
class Solution {
    
    private int find(int[] parent, int v) {
        if(parent[v] == v) {
            return v;
        }
        return parent[v] = find(parent, parent[v]);
    }
    
    private boolean union(int[] parent, int x, int y) {
        int xRoot = find(parent, x);
        int yRoot = find(parent, y);
        
        // They are in the same set. Cycle occurs
        if(xRoot == yRoot) {
            return false;
        } 
        
        parent[yRoot] = xRoot;
        return true;
    }
    public int countComponents(int n, int[][] edges) {
        int[] parent = new int[n];
        
        // initialise the parent arr with the index, means parent of i is the index 'i' itself
        for(int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        int noOfComponents = n;
        
        for(int[] edge: edges) {
            if(union(parent, edge[0], edge[1])) {
                noOfComponents--;
            }
        }
        
        return noOfComponents;
    }
}
```


