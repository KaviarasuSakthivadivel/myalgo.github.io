# Depth First Search

Depth First search questions, 
1. check if the path exists from source to destination. 
2. Print all the paths from source to destination. 

In general, DFS can be used to check if the path exist between two nodes. We can also use Union Find to check if there exists a path between two nodes! Hint: Use **areConnected()** method. 


### Find if Path Exists in Graph

There is a **bi-directional** graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [ui, vi]` denotes a bi-directional edge between vertex `ui` and vertex `vi`. Every vertex pair is connected by **at most one** edge, and no vertex has an edge to itself.

You want to determine if there is a **valid path** that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true` _if there is a **valid path** from_ `source` _to_ `destination`_, or_ `false` _otherwise_

**Input:** n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
**Output:** true
**Explanation:** There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

![[validpath-ex1.png]]

**Input:** n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]  , source = 0, destination = 5
**Output:** false
**Explanation:** There is no path from vertex 0 to vertex 5.
![[validpath-ex2.png]]


```java

public class ValidPath {

    private static boolean validPathUsingDFSIterative(int[][] edges, int n, int source, int destination) {
        // Using DFS, we can find out if there exists a path from source to destination.

        Stack<Integer> stack = new Stack<>();

        // Construct an Adjacency list, since it is an undirected graph
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        for(int[] edge : edges) {
            graph.computeIfAbsent(edge[0], l -> new LinkedList<>()).add(edge[1]);
            graph.computeIfAbsent(edge[1], l -> new LinkedList<>()).add(edge[0]);
        }

        // To capture it's already visited or not.
        HashSet<Integer> seen = new HashSet<>();

        stack.push(source);

        while(!stack.isEmpty()) {
            int u = stack.pop();

            if(u == destination) {
                return true;
            }

            if(seen.add(u)) {
                if(graph.containsKey(u)) {
                    stack.addAll(graph.get(u));
                }
            }
        }

        return false;
    }

    public static boolean validPathUsingDFS(int[][] edges, int n, int source, int destination) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        boolean[] visited = new boolean[n];
        for(int[] edge : edges) {
            int a = edge[0], b = edge[1];

            graph.computeIfAbsent(a, val -> new LinkedList<>()).add(b);
            graph.computeIfAbsent(b, val -> new LinkedList<>()).add(a);
        }

        return dfsRecursive(graph, visited, source, destination);
    }

    private static boolean dfsRecursive(Map<Integer, List<Integer>> graph, boolean[] visited, int currentNode, int end) {
        // check if the current node reached destination.
        if(currentNode == end) {
            return true;
        }

        if(!visited[currentNode]) {
            visited[currentNode] = true;
            // check for all the neighbour nodes
            for(int v : graph.get(currentNode)) {
                if(dfsRecursive(graph, visited, v, end)) {
                    return true;
                }
            }
        }
        return false;
    }

    private static boolean validPathBFS(int[][] edges, int n, int source, int destination) {
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        for(int[] edge : edges) {
            graph.computeIfAbsent(edge[0], l -> new LinkedList<>()).add(edge[1]);
            graph.computeIfAbsent(edge[1], l -> new LinkedList<>()).add(edge[0]);
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(source);

        HashSet<Integer> seen = new HashSet<>();
        seen.add(source);

        while(!queue.isEmpty()) {
            Integer u = queue.poll();

            if(u == destination) {
                return true;
            }

            for(int v : graph.get(u)) {
                if(!seen.contains(v)) {
                    queue.offer(v);
                    seen.add(v);
                }
            }
        }

        return false;
    }

    public static void main(String[] args) {
        int[][] edges = new int[][] {
                {0, 1}, {1, 2}, {2, 0}
        };
        int n = 3;
        System.out.println(validPathUsingDFSIterative(edges, n, 0, 2));

        edges = new int[][] {
                {0, 1}, {0, 2}, {3, 5}, {5, 4}, {4, 3}
        };
        n = 6;
        System.out.println(validPathUsingDFSIterative(edges, n, 0, 5));

        edges = new int[][] {
                {0, 1}, {1, 2}, {2, 0}
        };
        n = 3;
        System.out.println(validPathUsingDFS(edges, n, 0, 2));

        edges = new int[][] {
                {0, 1}, {0, 2}, {3, 5}, {5, 4}, {4, 3}
        };
        n = 6;
        System.out.println(validPathUsingDFS(edges, n, 0, 5));
    }
}

```

### All Paths From Source to Target

Given a directed acyclic graph (**DAG**) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in **any order**.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node `graph[i][j]`).


**Input:** graph = [[1,2],[3],[3],[]]
**Output:** [[0,1,3],[0,2,3]]
**Explanation:** There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

![[all_1.jpeg]]


```java
public class AllPathSourceTarget {  
  
    // Source is 0 to n - 1  
    private static List<List<Integer>> allPathsSourceTarget(int[][] graph) {  
        // Do DFS, keep the current path in the list. Add / Remove while processing parallel nodes.  
  
        List<List<Integer>> paths = new ArrayList<>();  
        List<Integer> path = new ArrayList<>();  
  
        dfs(graph, 0, path, paths);  
        return paths;  
    }  
  
    private static void dfs(int[][] graph, int u, List<Integer> path, List<List<Integer>> paths) {  
        // Add the node to the path  
        path.add(u);  
  
        if(u == graph.length - 1) {  
            paths.add(new ArrayList<>(path));  
            return;        
        }  
  
        for(int v : graph[u]) {  
            dfs(graph, v, path, paths);  
            path.remove(path.size() - 1);  
        }  
    }  
  
    public static void main(String[] args) {  
        int[][] graph = new int[][]{  
                {1, 2}, {3}, {3}, {}  
        };  
  
        for(List<Integer> path : allPathsSourceTarget(graph)) {  
            System.out.println(path);  
        }  
    }  
}
```

### 1059. All Paths from Source Lead to Destination

Given the `edges` of a directed graph where `edges[i] = [ai, bi]` indicates there is an edge between nodes `ai` and `bi`, and two nodes `source` and `destination` of this graph, determine whether or not all paths starting from `source` eventually, end at `destination`, that is:

- At least one path exists from the `source` node to the `destination` node
- If a path exists from the `source` node to a node with no outgoing edges, then that node is equal to `destination`.
- The number of possible paths from `source` to `destination` is a finite number.

Return `true` if and only if all roads from `source` lead to `destination`.

#### Thoughts
			Problem simply boils down to two things which we need to check during our graph traversal algorithm. We need to detect any cycles in the traversal and return false if there are any. Also, we need to ensure that if there is a leaf node encountered during the traversal, it is the destination node.

```java
class Solution {
    enum Color {
        GREY, BLACK
    };
    
    public boolean leadsToDestination(int n, int[][] edges, int source, int destination) {
        ArrayList<Integer>[] graph = buildGraph(edges, n);
        
        return dfs(graph, new Color[n], source, destination);
    }

    private boolean dfs(ArrayList<Integer>[] graph, Color[] color, int start, int end) {
        // to detect there is no loop
        if(color[start] != null) {
            return color[start] == Color.BLACK;
        }
        
        // leaf node, so check it has reached the destination node. 
        // out degree of this node must be zero
        if(graph[start].isEmpty()) {
            return start == end;
        }
        
        // We started processing for this node
        color[start] = Color.GREY;
        
        for(int neighbour : graph[start]) {
            if(!dfs(graph, color, neighbour, end)) {
                return false;
            }
        }
        
        // We completed processing for this node. 
        color[start] = Color.BLACK;
        
        return true;
    }
    
    private ArrayList<Integer>[] buildGraph(int[][] edges, int n) {
        ArrayList<Integer>[] graph = new ArrayList[n];
        
        for(int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for(int i = 0; i < edges.length; i++) {
            int[] edge = edges[i];
            graph[edge[0]].add(edge[1]);
        }
        
        return graph;
    }
}
```

# Breadth First Search

“Breadth-first search” algorithm can traverse all vertices of a “graph” and traverse all paths between two vertices. However, the most advantageous use case of “breadth-first search” is to efficiently find the shortest path between two vertices in a “graph” where **all edges have equal and positive weights**.

```java
private static boolean validPathBFS(int[][] edges, int n, int source, int destination) {  
    HashMap<Integer, List<Integer>> graph = new HashMap<>();  
    for(int[] edge : edges) {  
        graph.computeIfAbsent(edge[0], l -> new LinkedList<>()).add(edge[1]);  
        graph.computeIfAbsent(edge[1], l -> new LinkedList<>()).add(edge[0]);  
    }  
  
    Queue<Integer> queue = new LinkedList<>();  
    queue.offer(source);  
  
    HashSet<Integer> seen = new HashSet<>();  
    seen.add(source);  
  
    while(!queue.isEmpty()) {  
        Integer u = queue.poll();  
  
        if(u == destination) {  
            return true;  
        }  
  
        for(int v : graph.get(u)) {  
            if(!seen.contains(v)) {  
                queue.offer(v);  
                seen.add(v);  
            }  
        }  
    }  
  
    return false;  
}
```

## All Paths From Source to Target - BFS


```java
class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> paths = new ArrayList<>();
        if (graph == null || graph.length == 0) {
            return paths;
        }

        Queue<List<Integer>> queue = new LinkedList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        queue.add(path);

        while (!queue.isEmpty()) {
            List<Integer> currentPath = queue.poll();
            int node = currentPath.get(currentPath.size() - 1);
            for (int nextNode: graph[node]) {
                List<Integer> tmpPath = new ArrayList<>(currentPath);
                tmpPath.add(nextNode);
                if (nextNode == graph.length - 1) {
                    paths.add(new ArrayList<>(tmpPath));
                } else {
                    queue.add(new ArrayList<>(tmpPath));
                } 
            }
        }
        return paths;
    }
}
```



# Minimum Spanning Tree

![[6. GraphAlgorithms-NA.pdf]]


## Kruskal’s Algorithm

“Kruskal’s algorithm” is an algorithm to construct a “minimum spanning tree” of a “weighted undirected graph”.

### Find MST

```java

public class KruskalMST {  
    public void findMST(Graph graph) {  
        int V = graph.vertices;  
        int[] parents = new int[V];  
  
        for(int i = 0 ; i < V; i++) {  
            parents[i] = i;  
        }  
  
        PriorityQueue<WeightedEdge> pQueue = new PriorityQueue<>(graph.weightedEdges.size(), Comparator.comparingLong(e -> e.weight));  
        pQueue.addAll(graph.weightedEdges);  
        PriorityQueue<WeightedEdge> mst = new PriorityQueue<>(graph.weightedEdges.size(), Comparator.comparingInt(e -> e.source));  
  
        int total = 0;  
        while(pQueue.size() > 0) {  
            WeightedEdge weightedEdge = pQueue.remove();  
  
            int uSet = find(parents, weightedEdge.source);  
            int vSet = find(parents, weightedEdge.destination);  
  
            if(uSet != vSet) {  
                mst.add(weightedEdge);  
                total += weightedEdge.weight;  
                union(parents, uSet, vSet);  
            }  
        }  
//        System.out.println(mst.stream().mapToLong(e->e.weight).sum());  
        System.out.println(total);  
        for(WeightedEdge e : mst) {  
            System.out.println(e.toString());  
        }  
  
    }  
  
    public int find(int[] parents, int v) {  
        if(parents[v] != v) {  
            parents[v] = find(parents, parents[v]);  
        }  
        return parents[v];  
    }  
  
    public void union(int[] parents, int x, int y) {  
        int xRoot = find(parents, x);  
        int yRoot = find(parents, y);  
  
        if(xRoot != yRoot) {  
            parents[xRoot] = yRoot;  
        }  
    }  
  
    public static void main(String[] args) {  
        Graph graph = new Graph(15);  
        graph.addEdge(0, 1, 5);  
        graph.addEdge(1, 2, 8);  
        graph.addEdge(2, 3, 13);  
        graph.addEdge(3, 4, 9);  
        graph.addEdge(1, 7, 11);  
        graph.addEdge(0, 7, 12);  
        graph.addEdge(7, 8, 7);  
        graph.addEdge(8, 6, 6);  
        graph.addEdge(7, 6, 1);  
        graph.addEdge(2, 8, 2);  
        graph.addEdge(2, 5, 14);  
        graph.addEdge(6, 5, 3);  
        graph.addEdge(3, 5, 14);  
        graph.addEdge(5, 4, 10);  
  
        new KruskalMST().findMST(graph);  
    }  
  
    static class Graph {  
        int vertices;  
        ArrayList<WeightedEdge> weightedEdges = new ArrayList<>();  
  
        public Graph(int vertices) {  
            this.vertices = vertices;  
        }  
  
        public void addEdge(int source, int destination, int weight) {  
            WeightedEdge weightedEdge = new WeightedEdge(source, destination, weight);  
            weightedEdges.add(weightedEdge);  
        }  
    }  
  
    static class WeightedEdge {  
        int source;  
        int destination;  
        long weight;  
  
        public WeightedEdge(int source, int destination, int weight) {  
            this.source = source;  
            this.destination = destination;  
            this.weight = weight;  
        }  
  
        @Override  
        public String toString() {  
            return source + " " + destination;  
        }  
    }  
}

```

### 1584. Min Cost to Connect All Points

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **manhattan distance** between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return _the minimum cost to make all points connected._ All points are connected if there is **exactly one** simple path between any two points.

![[Min-Cost-to-Connect-All-Points.png]]

**Input:** points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
**Output:** 20
**Explanation:**

![[min-cost-2.png]]

```java

class Solution {
    // Solving by finding the minimum spanning tree.
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        UnionFind uFind = new UnionFind(n);
        
        PriorityQueue<Edge> queue = new PriorityQueue<>(Comparator.comparingInt(e -> e.getWeight()));
        
        for(int i = 0; i < n; i++) {
            int[] coord1 = points[i];
            
            for(int j = i + 1; j < n; j++) {
                int[] coord2 = points[j];
                
                int distance = Math.abs(coord1[0] - coord2[0]) + Math.abs(coord1[1] - coord2[1]);
                queue.add(new Edge(i, j, distance));
            }
        }
        
        // We can stop the loop when we have reached n - 1 nodes connection in MST
        int count = n - 1;
        int result = 0;
        while(!queue.isEmpty() && count > 0) {
            Edge e = queue.poll();
            
            if(!uFind.areConnected(e.getSource(), e.getDestination())) {
                uFind.union(e.getSource(), e.getDestination());
                result += e.getWeight();
            }
        }
        
        return result;
    }
}

class Edge {
    private int source;
    private int destination;
    private int weight;
    
    public Edge(int _source, int _destination, int _weight) {
        source = _source;
        destination = _destination;
        weight = _weight;
    }
    
    public int getWeight() {
        return weight;
    }
    
    public int getSource() {
        return source;
    }
    
    public int getDestination() {
        return destination;
    }
}

class UnionFind {
    private int[] root, rank;
    
    public UnionFind(int size) {
        this.root = new int[size];
        this.rank = new int[size];
        
        for(int i = 0; i < size; i++) {
            this.root[i] = i;
            this.rank[i] = 1;
        }
    }
    
    // Path compression technique
    public int find(int v) {
        if(v == root[v]) {
            return v;
        }
        
        return root[v] = find(root[v]);
    }
    
    // Rank technique, quick union
    public void union(int x, int y) {
        int xRoot = find(x);
        int yRoot = find(y);
        
        if(xRoot != yRoot) {
            if(rank[xRoot] < rank[yRoot]) {
                root[xRoot] = yRoot;
            } else if(rank[yRoot] < rank[xRoot]) {
                root[yRoot] = xRoot;
            } else {
                root[xRoot] = yRoot;
                rank[yRoot] += 1;
            }
        }
    }
    
    public boolean areConnected(int x, int y) {
        return find(x) == find(y);
    }
}

```


# Single Source Shortest Path

“Breadth-first search” algorithm to find the “shortest path” between two vertices. However, the “breadth-first search” algorithm can only solve the “shortest path” problem in “unweighted graphs”. But in real life, we often need to find the “shortest path” in a “weighted graph”.

For example, there may be many routes from your home to a target location, such as a bus station, and the time needed for each route may be different. The route with the shortest distance may not be the one that requires the least amount of time because of the speed limit and traffic jams. So, if we want to find the route that takes the least time from home to a certain bus station, then the weights should be time instead of distance. With that in mind, how can we solve the “shortest path” problem given two vertices in a “weighted graph”?

1. Dijkstra’s algorithm
2. Bellman-Ford algorithm

“Dijkstra's algorithm” can only be used to solve the “single source shortest path” problem in a graph with non-negative weights.

“Bellman-Ford algorithm”, on the other hand, can solve the “single-source shortest path” in a weighted directed graph with any weights, including, of course, negative weights.

