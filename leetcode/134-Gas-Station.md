# 134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:

    Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3
    Explanation:
    Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    Travel to station 4. Your tank = 4 - 1 + 5 = 8
    Travel to station 0. Your tank = 8 - 2 + 1 = 7
    Travel to station 1. Your tank = 7 - 3 + 2 = 6
    Travel to station 2. Your tank = 6 - 4 + 3 = 5
    Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
    Therefore, return 3 as the starting index.


### Solution 
Now the algorithm is straightforward :

Initiate total_tank and curr_tank as zero, and choose station 0 as a starting station.

Iterate over all stations :

1. Update total_tank and curr_tank at each step, by adding gas[i] and subtracting cost[i].

2. If curr_tank < 0 at i + 1 station, make i + 1 station a new starting point and reset curr_tank = 0 to start with an empty tank.

3. Return -1 if total_tank < 0 and starting station otherwise.



```java
public int canCompleteCircuit(int[] gas, int[] cost) {
    int n = gas.length;
    int startStation = 0;
    int currentTank = 0;
    int totalTank = 0;
    
    for(int i = 0; i < n; i++) {
        currentTank += gas[i] - cost[i];
        totalTank += gas[i] - cost[i];
        
        if(currentTank < 0) {
            startStation = i + 1;
            currentTank = 0;
        }
    }
    
    return totalTank >= 0 ? startStation : -1;
    
}
```