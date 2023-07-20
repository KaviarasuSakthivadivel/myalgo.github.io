Given a set of buildings in an array, process the buildings from east to west and return the list of buildings that have a sunset view. If a building is shorter than another building to its west then it looses its sunset view.

```java
class Program {

    public ArrayList<Integer> sunsetViews(int[] buildings, String direction) {
        ArrayList <Integer> result = new ArrayList<Integer>();

        int n = buildings.length;
        int step = direction.equals("WEST") ? 1 : -1;
        int startIdx = direction.equals("WEST") ? 0 : n - 1;

        int runningMaxHeight = 0;

        while(startIdx >= 0 && startIdx < n) {
            int currentBuildingHeight = buildings[startIdx];

            if(currentBuildingHeight > runningMaxHeight) {
                result.add(startIdx);
            }

            runningMaxHeight = Math.max(runningMaxHeight, currentBuildingHeight);
            startIdx += step;
        }

        if(direction.equals("EAST")) {
            Collections.reverse(result);
        }

        return result;
    }
}
```

