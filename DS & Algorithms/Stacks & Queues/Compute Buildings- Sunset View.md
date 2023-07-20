# **Compute Buildings w/ a Sunset View**

---

You are provided an array `buildings` of non-negative integers where each item represents the height of a building on a skyline from left to right:

- The sun sits on the far left
- A building is "blocked" from seeing the sun if there is a building **to its left** that is **>=** **in height** than itself

Return a revised list with all buildings blocked from the sun removed, denoting each unblocked building by its original index in the `buildings` list. Maintain the relative ordering of the buildings in the returned list.

**Input-Output**

**Example 1**

```javascript
Input: [11, 12, 13, 14, 15]
Output: [0, 1, 2, 3, 4]
Explanation: No building is blocked, all buildings have a sunset view.
```

**Example 2**

```javascript
Input: [7, 4, 8, 2, 9]
Output: [0, 2, 4]

Explanation:
- Building at index 1 (value 4) is blocked by building at index 0 (value 7) because 7 >= 4.
- Building at index 3 (value 2) is blocked by building at index 2 (value 8) because 8 >= 2.
```

### Solution



```java

public class SunsetViews {

    public static int[] completeBuildingsWithSunsetViews(int[] buildings) {

        // Stack will hold all the buildings that can see the sunset at the end of the loop.
        int n = buildings.length;

        Stack<Integer> stack = new Stack<>();
        for(int i = n - 1; i >= 0; i--) {
            int currentBuildingHeight = buildings[i];
            while(!stack.isEmpty() && currentBuildingHeight >= buildings[stack.peek()]) { // Current building is blocking the view
                stack.pop();
            }

            stack.push(i);
        }

        int[] result = new int[stack.size()];
        int idx = stack.size() - 1;
        while(!stack.isEmpty()) {
            result[idx] = stack.pop();
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(completeBuildingsWithSunsetViews(new int[] {7, 4, 8, 2, 9})));
    }
}

```