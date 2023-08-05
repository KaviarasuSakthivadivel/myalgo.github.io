
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

            if(!seen.add(u)) {
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

## Important Questions

[[329. Longest Increasing Path in a Matrix]]
[[694. Number of Distinct Islands]]

# Breadth First Search

### Template I

---

```java
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    // BFS
    while (queue is not empty) {
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                add next to queue;
            }
            remove the first node from queue;
        }
        step = step + 1;
    }
    return -1;          // there is no path from root to target
}
```

### Template II

---

Sometimes, it is important to make sure that we `never visit a node twice`. Otherwise, we might get stuck in an infinite loop, _e.g._ in graph with cycle. If so, we can add a hash set to the code above to solve this problem. Here is the pseudocode after modification:

```java
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    Set<Node> visited;  // store all the nodes that we've visited
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    add root to visited;
    // BFS
    while (queue is not empty) {
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                if (next is not in visited) {
                    add next to queue;
                    add next to visited;
                }
            }
            remove the first node from queue;
        }
        step = step + 1;
    }
    return -1;          // there is no path from root to target
}
```


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


## Important Question

1. [[1319. Number of Operations to Make Network Connected]]
2. [[1730. Shortest Path to Get Food]]
3. [[1293. Shortest Path in a Grid with Obstacles Elimination]]
4. 

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

### 743. Network Delay Time

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return _the **minimum** time it takes for all the_ `n` _nodes to receive the signal_. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

**Input:** times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
**Output:** 2

![[931_example_1.png]]

**Thoughts**

1. Create graph! Adjacency list, which is a **HashMap of u, Pair (Network Time, v)**
2. Have a **signalReceivedAt** array of length n + 1, since it is 1-indexed. Initialise it as Max_Value.
3. Call, BFS which is `dijkstra` method here and initialise **pq** Priority Queue, which is a pair of (Network Time, vertices) 
4. Initialise signalReceivedAt[0] = 0, because distance for source to source is zero. And add it to priority queue **pq**
5. Repeat until, the queue is not empty. 
	1. Remove the first inserted element as **u = pq.remove()**
	2. If u -> time is greater than the signalReceivedAt[u], continue the loop!
	3. else, **for each v in graph.get(u)** do, 
		1. if **u -> time + v -> time** less than signalReceivedAt[v] then update the value of signalReceivedAt[v] = **u -> time + v -> time**. Then add v into queue with the pair of **signalReceivedAt[v], v**

```java

class Solution {
    // Adjacency list
    Map<Integer, List<Pair<Integer, Integer>>> adj = new HashMap<>();
    
    private void dijkstra(int[] signalReceivedAt, int source, int n) {
        Queue<Pair<Integer, Integer>> pq = new PriorityQueue<Pair<Integer,Integer>>
            (Comparator.comparing(Pair::getKey));
        pq.add(new Pair(0, source));
        
        // Time for starting node is 0
        signalReceivedAt[source] = 0;
        
        while (!pq.isEmpty()) {
            Pair<Integer, Integer> topPair = pq.remove();
            
            int u = topPair.getValue();
            int uTime = topPair.getKey();
            
            if (uTime > signalReceivedAt[u]) {
                continue;
            }
            
            // Broadcast the signal to adjacent nodes
            for (Pair<Integer, Integer> edge : adj.getOrDefault(u, new ArrayList<Pair<Integer, Integer>>())) {
                int vTime = edge.getKey();
                int v = edge.getValue();
                
                // Fastest signal time for v so far
                // signalReceivedAt[currNode] + time : 
                // time when signal reaches v
                if (signalReceivedAt[v] > uTime + vTime) {
                    signalReceivedAt[v] = uTime + vTime;
                    pq.add(new Pair(signalReceivedAt[v], v));
                }
            }
        }
    }
    
    public int networkDelayTime(int[][] times, int n, int k) {
        // Build the adjacency list
        for (int[] time : times) {
            int source = time[0];
            int dest = time[1];
            int travelTime = time[2];
            
            adj.computeIfAbsent(source, l -> new ArrayList<>()).add(new Pair(travelTime, dest));
        }
        
        int[] signalReceivedAt = new int[n + 1];
        Arrays.fill(signalReceivedAt, Integer.MAX_VALUE);
        
        dijkstra(signalReceivedAt, k, n);
        
        int answer = Integer.MIN_VALUE;
        for (int i = 1; i <= n; i++) {
            answer = Math.max(answer, signalReceivedAt[i]);
        }
        
        // INT_MAX signifies atleat one node is unreachable
        return answer == Integer.MAX_VALUE ? -1 : answer;
    }
}

```


# Bellman Ford Algorithm

“Dijkstra algorithm” is restricted to solving the “single source shortest path” problem in graphs without negative weights. So, how could we solve the “single source shortest path” problem in graphs with negative weights?

**Theorem 1: In a “graph with no negative-weight cycles” with N vertices, the shortest path between any two vertices has at most N-1 edges.**

**Theorem 2: In a “graph with negative weight cycles”, there is no shortest path.**

#### How does the Bellman-Ford algorithm detect “negative weight cycles”?

---

Although the “Bellman-Ford algorithm” cannot find the shortest path in a graph with “negative weight cycles”, it can detect whether there exists a “negative weight cycle” in the “graph”.

**Detection method**: After relaxing each edge `N-1` times, perform the `N`th relaxation. According to the “Bellman-Ford algorithm”, all distances must be the shortest after relaxing each edge `N-1` times. However, after the `N`th relaxation, if there exists `distances[u] + weight(u, v) < distances(v)` for any `edge(u, v)`, it means there is a shorter path . At this point, we can conclude that there exists a “negative weight cycle”.

### 787. Cheapest Flights Within K Stops

There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [fromi, toi, pricei]` indicates that there is a flight from city `fromi` to city `toi` with cost `pricei`.

You are also given three integers `src`, `dst`, and `k`, return _**the cheapest price** from_ `src` _to_ `dst` _with at most_ `k` _stops._ If there is no such route, return `-1`.

**Input:** n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
**Output:** 700
**Explanation:**
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

![[cheapest-flights-within-k-stops-3drawio.png]]

#### Intuition
Bellman Ford's algorithm is used to find the shortest paths from the source node to all other vertices in a weighted graph. It depends on the idea that the shortest path contains at most `N - 1` edges (where `N` is the number of nodes in the graph) because the shortest path cannot have a cycle.

This algorithm takes as input a directed weighted graph and a starting node. It produces all the shortest paths from the starting node to all other vertices. It initially sets the distance from the starting node to all other vertices to infinity. The distance of the starting node is set to `0`. The algorithm loops through each edge `N - 1` times. If it finds an edge through which the distance of a node is smaller than the previously stored value, it uses this edge and stores the new value. This is called **relaxing** an edge.

It first calculates the shortest distances with at-most one edge in the path from the source. Then, it calculates the shortest paths with at-most `2` edges, and so on. After the `i-th` iteration over the edges, the shortest paths with at most `i` edges are calculated. There can be a maximum `N – 1` edges in any simple path (not a negative cycle), and that is why the algorithm iterates `N – 1` times over the edges.

Since we are limited to `k` stops, we can modify this algorithm to restrict the maximum number of edges that can be in a path to `k + 1`.

```java

class Solution {
    public int findCheapestPriceUsingTempArray(int n, int[][] flights, int src, int dst, int K) {
        Graph graph = new Graph(n);

        for(int[] edge : flights) {
            graph.addEdge(edge[0], edge[1], edge[2]);
        }

        int[] d = new int[n];
        Arrays.fill(d, Integer.MAX_VALUE);

        // Distance for src is always zero!
        d[src] = 0;

        for(int i = 0; i <= K; i++) {
            int[] tempD = Arrays.copyOf(d, n);
            for(WeightedEdge edge : graph.edges) {
                int u = edge.source;
                int v = edge.destination;
                int uVWeight = edge.weight;

                if(d[u] != Integer.MAX_VALUE) {
                    tempD[v] = Math.min(tempD[v], d[u] + uVWeight);
                }
            }
            
            d = tempD;
        }

        return d[dst] == Integer.MAX_VALUE ? -1 : d[dst];
    }

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        long[][] distance = new long[2][n];
        
        Arrays.fill(distance[0], Integer.MAX_VALUE);
        Arrays.fill(distance[1], Integer.MAX_VALUE);
        
        distance[0][src] = distance[1][src] = 0;
        
        for(int l = 0 ; l < K + 1; l++) {
            for(int[] edge : flights) {
                int u = edge[0];
                int v = edge[1];
                int wUV = edge[2];
                
                long dU = distance[1 - l & 1][u];
                long dV = distance[l & 1][v];

                if (dU + wUV < dV)
                    distance[l & 1][v] = dU + wUV;
            }
        }
        return distance[K & 1][dst] < Integer.MAX_VALUE ? (int) distance[K & 1][dst] : -1;
    }

    static class Graph {
        int vertices;
        ArrayList<WeightedEdge> edges;

        public Graph(int vertices) {
            this.vertices = vertices;
            edges = new ArrayList<>();
        }

        public void addEdge(int source, int destination, int weight) {
            edges.add(new WeightedEdge(source, destination, weight));
        }
    }

    static class WeightedEdge {
        int source;
        int destination;
        int weight;

        public WeightedEdge(int source, int destination, int weight) {  
            this.source = source;  
            this.destination = destination;  
            this.weight = weight;  
        } 

        @Override  
        public String toString() {  
            return "Edge{" + "source=" + source +  
                    ", destination=" + destination +  
                    ", weight=" + weight +  
                    '}';  
        }  
    }
}

```

###  Path With Minimum Effort
You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size `rows x columns`, where `heights[row][col]` represents the height of cell `(row, col)`. You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the bottom-right cell, `(rows-1, columns-1)` (i.e., **0-indexed**). You can move **up**, **down**, **left**, or **right**, and you wish to find a route that requires the minimum **effort**.

A route's **effort** is the **maximum absolute difference** in heights between two consecutive cells of the route.

Return _the minimum **effort** required to travel from the top-left cell to the bottom-right cell._

**Input:** heights = [[1,2,2],[3,8,2],[5,3,5]]
**Output:** 2
**Explanation:** The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

![[Path-With-Minimum-Effort-1.png]]
#### Intuition
Using BFS traversal, update the neighbouring cells based on the absolute difference current cell value and neighbouring cell's value in differenceMatrix 2d array! 

While traversing, if it has reached the bottom cell, return the max difference in the QNode. 

```java

class Solution {
    int directions[][] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public int minimumEffortPath(int[][] heights) {
        int row = heights.length;
        int col = heights[0].length;
        int[][] differenceMatrix = new int[row][col];
        for (int[] eachRow : differenceMatrix)
            Arrays.fill(eachRow, Integer.MAX_VALUE);
        differenceMatrix[0][0] = 0;
        PriorityQueue<Cell> queue = new PriorityQueue<Cell>((a, b) -> (a.difference.compareTo(b.difference)));
        boolean[][] visited = new boolean[row][col];
        queue.add(new Cell(0, 0, differenceMatrix[0][0]));

        while (!queue.isEmpty()) {
            Cell curr = queue.poll();
            visited[curr.x][curr.y] = true;
            if (curr.x == row - 1 && curr.y == col - 1)
                return curr.difference;
            for (int[] direction : directions) {
                int adjacentX = curr.x + direction[0];
                int adjacentY = curr.y + direction[1];
                if (isValidCell(adjacentX, adjacentY, row, col) && !visited[adjacentX][adjacentY]) {
                    int currentDifference = Math.abs(heights[adjacentX][adjacentY] - heights[curr.x][curr.y]);
                    int maxDifference = Math.max(currentDifference, differenceMatrix[curr.x][curr.y]);
                    if (differenceMatrix[adjacentX][adjacentY] > maxDifference) {
                        differenceMatrix[adjacentX][adjacentY] = maxDifference;
                        queue.add(new Cell(adjacentX, adjacentY, maxDifference));
                    }
                }
            }
        }
        return differenceMatrix[row - 1][col - 1];
    }

    boolean isValidCell(int x, int y, int row, int col) {
        return x >= 0 && x <= row - 1 && y >= 0 && y <= col - 1;
    }
}

class Cell {
    int x;
    int y;
    Integer difference;

    Cell(int x, int y, Integer difference) {
        this.x = x;
        this.y = y;
        this.difference = difference;
    }

    public int getDifference() {
        return this.difference;
    }
}

```


### 1514. Path with Maximum Probability
You are given an undirected weighted graph of `n` nodes (0-indexed), represented by an edge list where `edges[i] = [a, b]` is an undirected edge connecting the nodes `a` and `b` with a probability of success of traversing that edge `succProb[i]`.

Given two nodes `start` and `end`, find the path with the maximum probability of success to go from `start` to `end` and return its success probability.

If there is no path from `start` to `end`, **return 0**. Your answer will be accepted if it differs from the correct answer by at most **1e-5**.

![[1558_ex1.png]]

#### Intuition

> If you are not familiar with the Bellman-Ford algorithm, please refer to our [Bellman-Ford Algorithm Explore Card](https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3864/). For the sake of brevity, we will focus only on the usage of Bellman-Ford and not the implementation details.

The algorithm works by relaxing edges in the graph, meaning that it tries to improve the shortest path estimate for each node in the graph until the solution is found.

Bellman-Ford is typically used to find the shortest path in a weighted graph. In this problem, instead of the shortest distance, we are looking for the **maximum probability**. The length of a path is the sum of the weights of its edges. Here, the probability of a path equals the product of the probabilities of its edges.

Initially, we set the probability to reach the starting node `start` as `1` and all other probabilities as `0`. Then we iteratively relax the edges of the graph by updating the probability to each node if a higher probability is found.

Considering that a path in the graph without a cycle contains at most `n - 1` edges, the process is repeated `n - 1` times, which is enough to relax every edge of every possible path.

- In the first round, we update the maximum probability of reaching each node `u` from the starting node along the path that contains only one edge `(u, v)`.
- In the second round, we update the maximum probability of reaching each node `u` from the starting node along the path that contains two edges (including `(u, v)`).
- and so on.

After `n - 1` rounds, we have updated `max_prob[end]` to be the maximum probability of reaching `end` from the staring node along every possible path.


**Solution**

1. Relax all edges: for each edge `(u, v)`, if a higher probability of reaching `u` through this edge is found, update the `max_prob[u]` as `max_prob[u] = max_prob[v] * path_prob`, if a higher probability to reach `v` through this edge is found, update the `max_prob[v]`.

```java

class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        double[] maxProb = new double[n];
        maxProb[start] = 1.0;

        // relax edges till n - 1
        for(int i = 0; i < n - 1; i++) {
            boolean updated = false;

            for(int edgeIdx = 0; edgeIdx < edges.length; edgeIdx++) {
                int u = edges[edgeIdx][0];
                int v = edges[edgeIdx][1];
                double uVProb = succProb[edgeIdx];

                if(maxProb[v] < uVProb * maxProb[u]) {
                    maxProb[v] = uVProb * maxProb[u];
                    updated = true;
                }
                if(maxProb[u] < uVProb * maxProb[v]) {
                    maxProb[u] = uVProb * maxProb[v];
                    updated = true;
                }
            }
            if(!updated) {
                break;
            }
        }
        return maxProb[end];
    }
}

```


# Overview of Kahn's Algorithm

When selecting courses for the next semester in college, you might have noticed that some advanced courses have prerequisites that require you to take some introductory courses first. In Figure 12, for example, to take Course C, you need to complete Course B first, and to take Course B, you need to complete Course A first. There are many courses that you must complete for an academic degree. You do not want to find out in the last semester that you have not completed some prerequisite courses for an advanced course. So, how can we arrange the order of the courses adequately while considering these prerequisite relationships between them?

![[Course_Relationships.png]]

“Topological sorting” helps solve the problem. It provides a linear sorting based on the required ordering between vertices in directed acyclic graphs. To be specific, given vertices `u` and `v`, to reach vertex `v`, we must have reached vertex `u` first. In “topological sorting”, `u` has to appear before `v` in the ordering. The most popular algorithm for “topological sorting” is Kahn’s algorithm.

### Limitation of the Algorithm

---

- “Topological sorting” only works with graphs that are directed and acyclic.
- There must be at least one vertex in the “graph” with an “in-degree” of 0. If all vertices in the “graph” have a non-zero “in-degree”, then all vertices need at least one vertex as a predecessor. In this case, no vertex can serve as the starting vertex.

### Course Schedule II

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return _the ordering of courses you should take to finish all courses_. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

**Example 1:**

**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** [0,1]
**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

```java

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] result = new int[numCourses];
        if (numCourses == 0) {
            return result;
        }
        
        if (prerequisites.length == 0) {
            for (int i = 0; i < numCourses; i++) {
                result[i] = i;
            }
            return result;
        }
        
        int[] indegree = new int[numCourses];
        Queue<Integer> zeroDegree = new LinkedList<>();
        HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();
        for (int[] pre : prerequisites) {
            int parent = pre[0], child = pre[1];
            graph.computeIfAbsent(child, val -> new ArrayList<>()).add(parent);
            indegree[parent]++;
        }
        for (int i = 0; i < indegree.length; i++) {
            if (indegree[i] == 0){
                zeroDegree.add(i);
            }
        }
        if (zeroDegree.isEmpty()) {
            return new int[0];
        }
        int index = 0;
        while (!zeroDegree.isEmpty()) {
            int u = zeroDegree.poll();
            result[index++] = u;

            if(graph.containsKey(u)) {
                for(int v : graph.get(u)) {
                    if(--indegree[v] == 0) {
                        zeroDegree.add(v);
                    }
                }
            }
        }
        
        for (int in : indegree) {
            if (in != 0) {
                return new int[0];
            }
        }

        return result;
    }
}

```


### Alien Dictionary
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are **sorted lexicographically** by the rules of this new language.

Return _a string of the unique letters in the new alien language sorted in **lexicographically increasing order** by the new language's rules._ If there is no solution, return `""`_._ If there are multiple solutions, return _**any of them**_.

**Example 1:**

**Input:** words = ["wrt","wrf","er","ett","rftt"]
**Output:** "wertf"

**Example 2:**

**Input:** words = ["z","x"]
**Output:** "zx"

```java

class Solution {
    public String alienOrder(String[] words) {
        HashMap<Character, ArrayList<Character>> graph = new HashMap<>();
        HashMap<Character, Integer> charCount = new HashMap<>();
        
        for(String word : words) {
            for(Character ch : word.toCharArray()) {
                graph.putIfAbsent(ch, new ArrayList<>());
                charCount.putIfAbsent(ch, 0);
            }
        }
        
        for(int i = 0; i < words.length - 1; i++) {
            String word1 = words[i];
            String word2 = words[i + 1];
            
            if(word1.length() > word2.length() && word1.startsWith(word2)) {
                return "";
            }
            
            for(int j = 0; j < Math.min(word1.length(), word2.length()); j++) {
                char ch1 = word1.charAt(j), ch2 = word2.charAt(j);
                if(ch1 != ch2) {
                    graph.get(ch1).add(ch2);
                    charCount.put(ch2, charCount.get(ch2) + 1);
                    break;
                }
            }
        }
        
        Queue<Character> queue = new LinkedList<>();
        for(Character c : charCount.keySet()) {
            if(charCount.get(c) == 0) {
                queue.offer(c);
            }
        }
        
        StringBuilder sb = new StringBuilder();
        while(!queue.isEmpty()) {
            Character topCh = queue.poll();
            sb.append(topCh);
            
            for(char ch : graph.get(topCh)) {
                charCount.put(ch, charCount.get(ch) - 1);
                if(charCount.get(ch).equals(0)) {
                    queue.offer(ch);
                }
            }
        }
        
        if(sb.length() < charCount.size()) {
            return "";
        }
        
        return sb.toString();
    }
}

```


### More questions

[[1857. Largest Color Value in a Directed Graph]]
[[2115. Find All Possible Recipes from Given Supplies]]

# Test Bipartite

A **bipartite graph** also called a **bi-graph**, is a set of graph vertices, i.e, points where multiple lines meet, decomposed into two disjoint sets, meaning they have no element in common, such that no two graph vertices within the same set are **adjacent**.

> **Adjacent nodes** are any two nodes that are connected by an edge.



[[886. Possible Bipartition]]