# 281. Zigzag Iterator
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

  v1 = [1, 2]        
  v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

### Thoughts
We can use two pointers to iterate through the list of lists. `p` will point to which list, and `q` will point to which indices in the current list. In order to do, zigzag traversal, we are using a 2-sized array to keep track of which index is being currently traversed in the list of lists. 


### Solution
```java
import java.util.ArrayList;
import java.util.List;

public class ZigzagIterator {
    List<List<Integer>> list = new ArrayList<>();
    int[] indices = new int[2];
    int p = 0; int q = 0;

    public ZigzagIterator(List<Integer> l1, List<Integer> l2) {
        list.add(l1);
        list.add(l2);
    }

    public int next() {
        int value = list.get(p).get(q);
        // Increment the index of the current list
        indices[p] = q + 1;

        // For zigzag travel, update p pointer.
        p = 1 - p;

        q = indices[p];
        return value;
    }

    public boolean hasNext() {
        if(list.get(p).size() > indices[p]) {
            return true;
        } else {
            p = 1 - p;
            q = indices[p];
            return list.get(p).size() > q;
        }
    }
}
```