# 1059. All Paths from Source Lead to Destination

Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi, and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually, end at destination, that is:

At least one path exists from the source node to the destination node
If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
The number of possible paths from source to destination is a finite number.
Return true if and only if all roads from source lead to destination.


Example 1:

Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
Output: false
Explanation: It is possible to reach and get stuck on both node 1 and node 2.

Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
Output: true

### Solution

Let's try to boil the problem down to simpler, more commonly understandable terms.

We are given a directed graph.
Also, as inputs we are provided a source and a destination.
We need to tell if all the paths from the source lead to the destination and and we can split this into a few criteria.
If a path exists from the source node to a node with no outgoing edges, then that node must be equal to destination. Here, we simply need to see that if a node does not have any neighbors in the adjacency list structure, then it has to be the destination or else we return false.
The number of possible paths from source to destination is a finite number. This simply means that the graph is actually a tree. Or in other words, there are no cycles in the graph. If there is a cycle in the graph, there would be an infinite number of paths from the source to the destination, as each would go around the cycle a different number of times.

### Thus, the problem simply boils down to two things which we need to check during our graph traversal algorithm. We need to detect any cycles in the traversal and return false if there are any. Also, we need to ensure that if there is a leaf node encountered during the traversal, it is the destination node.

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