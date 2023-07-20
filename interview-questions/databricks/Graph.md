You live in San Francisco city and want to minimize your commute time to the Databricks HQ.

Given a 2D matrix of the San Francisco grid and the time as well as cost matrix of all the available transportation
modes, return the fastest mode of transportation. If there are multiple such modes then return one with the least cost.

Rules:
1. The input grid represents the city blocks, so the commuter is only allowed to travel along the horizontal and vertical axes. 
Diagonal traversal is not permitted.
2. The commuter can only move to the neighboring cells with the same transportation mode.

Sample Input:

2D Grid:              Legend:
|3|3|S|2|X|X|         X = Roadblock
|3|1|1|2|X|2|         S = Source
|3|1|1|2|2|2|         D = Destination
|3|1|1|1|D|3|         1 = Walk, 2 = Bike, 3 = Car, 4 = Train
|3|3|3|3|3|4|
|4|4|4|4|4|4|

Transportation Modes:        ["Walk", "Bike", "Car", "Train"]
Cost Matrix (Dollars/Block): [0,      1,      3,     2]
Time Matrix (Minutes/Block): [3,      2,      1,     1]

NOTE: In this example, we are only counting the blocks between 'S' and 'D' to compute the minimum time & dollar cost.

Sample Output: Bike

### Solution

To find the fastest mode of transportation with the least cost, we can use Dijkstra's algorithm to find the shortest path in the grid. Here's the step-by-step process:

1. Convert the given 2D grid into a graph representation, where each cell represents a node in the graph, and the neighboring cells (up, down, left, right) are connected with edges. Assign weights to the edges based on the transportation mode (cost and time matrices).
    
2. Initialize the distance and cost arrays for each node in the graph. Set the distance of the source node (S) to 0 and the cost to reach the source node as 0 for all transportation modes.
    
3. Create a priority queue to store nodes based on their distance. Initialize it with the source node.
    
4. While the priority queue is not empty, do the following steps:
    
    - Pop the node with the minimum distance from the priority queue.
    - For each neighboring node, calculate the new distance and cost to reach that node using the transportation mode.
    - If the new distance is smaller than the current distance of the neighboring node, update its distance and cost.
    - Add the neighboring node to the priority queue.
5. After the algorithm finishes, the distance and cost arrays will contain the shortest distance and cost to reach each node from the source node.
    
6. Compare the cost and time values for each transportation mode at the destination node (D) and find the mode with the minimum time and cost. If there are multiple modes with the same minimum time, choose the one with the least cost.
    

In the given example, using Dijkstra's algorithm, we find that the shortest distance from the source (S) to the destination (D) is 5 blocks. The minimum time for each transportation mode at the destination node is as follows:

- Walk: 5 blocks * 1 minute/block = 5 minutes
- Bike: 5 blocks * 2 minutes/block = 10 minutes
- Car: 5 blocks * 1 minute/block = 5 minutes
- Train: 5 blocks * 1 minute/block = 5 minutes

The minimum time is 5 minutes, which can be achieved by either walking, using a car, or taking the train. Among these options, the transportation mode with the least cost is "Bike" with a cost of 5 blocks * $1/block = $5. Therefore, the fastest mode of transportation with the least cost is "Bike".


```java
import java.util.*;

class Node implements Comparable<Node> {
    int row;
    int col;
    int distance;
    int cost;
    int mode;

    public Node(int row, int col, int distance, int cost, int mode) {
        this.row = row;
        this.col = col;
        this.distance = distance;
        this.cost = cost;
        this.mode = mode;
    }

    @Override
    public int compareTo(Node other) {
        if (this.distance != other.distance) {
            return Integer.compare(this.distance, other.distance);
        } else {
            return Integer.compare(this.cost, other.cost);
        }
    }
}

public class FastestTransportationMode {

    private static final int[] ROW_OFFSETS = {-1, 0, 1, 0}; // Up, Right, Down, Left
    private static final int[] COL_OFFSETS = {0, 1, 0, -1}; // Up, Right, Down, Left

    private static int findFastestTransportationMode(int[][] grid, int[] costMatrix, int[] timeMatrix) {
        int numRows = grid.length;
        int numCols = grid[0].length;

        // Initialize distance and cost arrays
        int[][] distance = new int[numRows][numCols];
        int[][] cost = new int[numRows][numCols];
        for (int i = 0; i < numRows; i++) {
            Arrays.fill(distance[i], Integer.MAX_VALUE);
            Arrays.fill(cost[i], Integer.MAX_VALUE);
        }

        // Priority queue for Dijkstra's algorithm
        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.offer(new Node(0, 0, 0, 0, 0));

        while (!queue.isEmpty()) {
            Node curr = queue.poll();
            int currRow = curr.row;
            int currCol = curr.col;
            int currDistance = curr.distance;
            int currCost = curr.cost;
            int currMode = curr.mode;

            if (currRow == numRows - 1 && currCol == numCols - 1) {
                // Reached the destination node, no need to explore further
                break;
            }

            // Explore neighboring nodes
            for (int i = 0; i < 4; i++) {
                int newRow = currRow + ROW_OFFSETS[i];
                int newCol = currCol + COL_OFFSETS[i];

                if (isValidCell(newRow, newCol, numRows, numCols) && grid[newRow][newCol] != -1) {
                    int newDistance = currDistance + 1;
                    int newCost = currCost + costMatrix[currMode];
                    int newMode = grid[newRow][newCol];

                    if (newDistance < distance[newRow][newCol] || (newDistance == distance[newRow][newCol] && newCost < cost[newRow][newCol])) {
                        distance[newRow][newCol] = newDistance;
                        cost[newRow][newCol] = newCost;
                        queue.offer(new Node(newRow, newCol, newDistance, newCost, newMode));
                    }
                }
            }
        }

        // Check the transportation mode with the minimum time and cost at the destination node
        int destinationMode = grid[numRows - 1][numCols - 1];
        int destinationTime = distance[numRows - 1][numCols - 1] * timeMatrix[destinationMode];

        // Find the mode with the minimum time and cost
        int fastestMode = -1;
        int minTime = Integer.MAX_VALUE;
        for (int mode = 1; mode <= 4; mode++) {
            if (timeMatrix[mode] * distance[numRows - 1][numCols - 1] == destinationTime && costMatrix[mode] < minTime) {
                fastestMode = mode;
                minTime = costMatrix[mode];
            }
        }

        return fastestMode;
    }

    private static boolean isValidCell(int row, int col, int numRows, int numCols) {
        return row >= 0 && row < numRows && col >= 0 && col < numCols;
    }

    public static void main(String[] args) {
        int[][] grid = {
                {3, 3, -1, 2, -1, -1},
                {3, 1, 1, 2, -1, 2},
                {3, 1, 1, 2, 2, 2},
                {3, 1, 1, 1, -1, 3},
                {3, 3, 3, 3, 3, 4},
                {4, 4, 4, 4, 4, 4}
        };

        int[] costMatrix = {0, 1, 3, 2};
        int[] timeMatrix = {3, 2, 1, 1};

        int fastestMode = findFastestTransportationMode(grid, costMatrix, timeMatrix);
        System.out.println("Fastest transportation mode: " + fastestMode);
    }
}

```

The `findFastestTransportationMode` method takes the grid, cost matrix, and time matrix as inputs and returns the fastest mode of transportation. The main method demonstrates how to use this method with the given example.

