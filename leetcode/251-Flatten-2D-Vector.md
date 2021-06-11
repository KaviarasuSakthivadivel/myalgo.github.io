# 251. Flatten 2D Vector

Implement an iterator to flatten a 2d vector.
For example,
 
    Given 2d vector = [
        [1,2],
        [3],
        [4,5,6]
    ]
    
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

### Thoughts

Keep a two pointer called, `listNumber` which tells which row in the list is being iterated. Another pointer called `iterator` which tells the current position of element in the current row. To get the value, use `vector.get(listNumer).get(iterator)`. When the row is completely iterated, go to next row. Increment the `listNumber` when row is completely iterated. 

### Solution

```java
import java.util.*;

public class Vector2D implements Iterator<Integer> {
    List<List<Integer>> vector = new ArrayList<>();
    int listNumber = 0; // Which list in the array list
    int iterator = 0; // Which item in the current list

    public Vector2D(List<List<Integer>> list) {
        for(List<Integer> currentList : list) {
            if(currentList.size() > 0) {
                vector.add(currentList);
            }
        }
    }

    @Override
    public boolean hasNext() {
        if(listNumber >= vector.size()) {
            return false;
        }
        return listNumber != vector.size() - 1 || iterator < vector.get(listNumber).size();
    }

    @Override
    public Integer next() {
        Integer val = vector.get(listNumber).get(iterator);
        iterator++;

        if(iterator == vector.get(listNumber).size()) {
            listNumber++;
            iterator = 0;
        }

        return val;
    }

    public static void main(String[] args) {
        List<List<Integer>> list = new ArrayList<>();
        List<Integer> one = new ArrayList<>();
        one.add(1);
        one.add(2);
        list.add(one);
        list.add(new ArrayList<>(Collections.singletonList(3)));

        List<Integer> second = new ArrayList<>();
        second.add(4);
        second.add(5);
        second.add(6);
        list.add(second);
        Vector2D vector2D = new Vector2D(list);
        while(vector2D.hasNext()) {
            System.out.print(vector2D.next() + ", ");
        }
    }
}
```