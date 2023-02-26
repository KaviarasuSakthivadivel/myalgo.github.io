# 1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


    Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20

### Solution
This problem is similar to finding Minimum spanning tree by Kruskal's method. Here we have given the points and we are asked to find the minimum cost.

1. Loop through the points and find distances and save it using the Edge data structure.
2. As we loop along, we add all the points to the Priority list which sorts the list based on the distance(weight)
3. Then, use the UnionFind data structure to find the MST. 
4. One trick here, we can stop calculating or joining the nodes once we have connected N - 1 nodes

MST is for the undirected weight graph. 

```java
class Solution {
    // Solving by finding the minimum spanning tree.
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        UnionFind uFind = new UnionFind(n);
        
        PriorityQueue<Edge> queue = new PriorityQueue<>((a, b) -> a.getWeight() - b.getWeight());
        
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