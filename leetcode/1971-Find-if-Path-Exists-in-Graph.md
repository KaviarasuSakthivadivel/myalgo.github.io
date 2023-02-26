# 1971. Find if Path Exists in Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.


    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: true
    Explanation: There are two paths from vertex 0 to vertex 2:
    - 0 → 1 → 2
    - 0 → 2

### Solution

### Using DFS and UnionFind

```java
class Solution {
    boolean hasPath = false;
    
    // Using DFS solution, it will be slow when compared to UnionFind algo
    public boolean validPathUsingDFS(int n, int[][] edges, int source, int destination) {
        ArrayList<Integer>[] graph = new ArrayList[n];
        
        for(int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for(int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }
        boolean[] visited = new boolean[n];
        
        dfs(graph, visited, source, destination);
        return hasPath;
    }
    
    private void dfs(ArrayList<Integer>[] graph, boolean[] visited, int start, int end) {
        if(!visited[start] && !hasPath) {
            if(start == end) {
                hasPath = true;
                return;
            }
            
            visited[start] = true;
            
            for(int v : graph[start]) {
                dfs(graph, visited, v, end);
            }
        }
    }
    
    // Using UnionFind algo
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        UnionFind uFind = new UnionFind(n);
        
        for(int[] edge : edges) {
            uFind.union(edge[0], edge[1]);
        }
        
        return uFind.areConnected(source, destination);
    }
}

class UnionFind {
    int size;
    int[] root;
    int[] rank;
    
    public UnionFind(int _size) {
        size = _size;
        root = new int[size];
        rank = new int[size];
        
        for(int i = 0; i < size; i++) {
            root[i] = i;
            rank[i] = 0;
        }
    }
    
    public int find(int v) {
        if(v != root[v]) {
            root[v] = find(root[v]);
        }
        return root[v];
    }
    
    // Optimised by rank function
    public boolean union(int x, int y) {
        int xRoot = find(x);
        int yRoot = find(y);
        
        // they are already in the same set
        if(xRoot == yRoot) {
            return false;
        }
        
        if(rank[xRoot] < rank[yRoot]) {
            root[xRoot] = yRoot;
        } else if(rank[yRoot] < rank[xRoot]) {
            root[yRoot] = xRoot;
        } else {
            root[xRoot] = yRoot;
            rank[yRoot] += 1;
        }
        
        return true;
    }
    
    public boolean areConnected(int x, int y) {
        return find(x) == find(y);
    }
}
```

### Using BFS
```java
class Solution {
    public boolean validPath(int n, int[][] edges, int start, int end) {
        List<List<Integer>> adjacency_list = new ArrayList<>();        
        for (int i = 0; i < n; i++) {
            adjacency_list.add(new ArrayList<>());
        }
        
        for (int[] edge : edges) {
            adjacency_list.get(edge[0]).add(edge[1]);
            adjacency_list.get(edge[1]).add(edge[0]);
        }
        
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        boolean seen[] = new boolean[n];
        Arrays.fill(seen, false);
        seen[start] = true;
        
        while (!queue.isEmpty()) {
            // Get the current node.
            int node = queue.poll();
            
            // Check if we have reached the target node.
            if (node == end) {
                return true;
            }
            
            // Add all neighbors to the stack.
            for (int neighbor : adjacency_list.get(node)) {
                // Check if neighbor has been added to the queue before.
                if (!seen[neighbor]) {
                    seen[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }
        
        return false;
    }
}
```