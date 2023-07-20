
# 362. Design Hit Counter

Design a hit counter which counts the number of hits received in the past `5` minutes (i.e., the past `300` seconds).

Your system should accept a `timestamp` parameter (**in seconds** granularity), and you may assume that calls are being made to the system in chronological order (i.e., `timestamp` is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the `HitCounter` class:

- `HitCounter()` Initializes the object of the hit counter system.
- `void hit(int timestamp)` Records a hit that happened at `timestamp` (**in seconds**). Several hits may happen at the same `timestamp`.
- `int getHits(int timestamp)` Returns the number of hits in the past 5 minutes from `timestamp` (i.e., the past `300` seconds).

Intuition: Store the incoming timestamps in an array. Timestamps are monotonically increasing, so the resulting array will be sorted in increasing order. Once you'd like to get the number of hits within the last 300 seconds, find the cutoff index at `timestamp - 300` in the sorted array. The timestamps to the right of this cutoff occurred within the 300 seconds. The length of the array minus the cutoff index gives you the count of these timestamps within 300 seconds. Done!

```rust
class HitCounter:
def __init__(self):
    self.hits = []

def hit(self, timestamp: int) -> None:
    self.hits.append(timestamp)

def getHits(self, timestamp: int) -> int:
    left, right = 0, len(self.hits) - 1
    target = timestamp - 300
    
    while left <= right:
        mid = (left + right) // 2

        if self.hits[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    
    return len(self.hits) - left
```

```java
class HitCounter {
    private Queue<Integer> hits; 

    /** Initialize your data structure here. */
    public HitCounter() {
        this.hits = new LinkedList<Integer>();
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        this.hits.add(timestamp);
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        while (!this.hits.isEmpty()) {
            int diff = timestamp - this.hits.peek();
            if (diff >= 300) this.hits.remove();
            else break;
        }
        return this.hits.size();
    }
}
```


### Fancy without any DS

O(s) s is total seconds in given time interval, in this case 300.  
basic ideal is using buckets. 1 bucket for every second because we only need to keep the recent hits info for 300 seconds. hit[] array is wrapped around by mod operation. Each hit bucket is associated with times[] bucket which record current time. If it is not current time, it means it is 300s or 600s... ago and need to reset to 1.

```java
public class HitCounter {
    private int[] times;
    private int[] hits;
    /** Initialize your data structure here. */
    public HitCounter() {
        times = new int[300];
        hits = new int[300];
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        int index = timestamp % 300;
        if (times[index] != timestamp) {
            times[index] = timestamp;
            hits[index] = 1;
        } else {
            hits[index]++;
        }
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        int total = 0;
        for (int i = 0; i < 300; i++) {
            if (timestamp - times[i] < 300) {
                total += hits[i];
            }
        }
        return total;
    }
}
```

### Multithreaded
What if there is 1000 hit(5) at time 5? Will there be a concurrent issue that many threads are trying to increment hit[5]? (In this problem, it seems there's no multi thread situation; however for a general hit counter, I think it will be a multithread.)

```java
import java.util.concurrent.atomic.AtomicIntegerArray;

public class HitCounter {
	AtomicIntegerArray time;
	AtomicIntegerArray hit;
    /** Initialize your data structure here. */
    public HitCounter() {
        time  = new AtomicIntegerArray(300);
        hit = new AtomicIntegerArray(300);
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
    	int index = timestamp % 300;
    	if (time.get(index) != timestamp) {
    		time.set(index, timestamp);
    		hit.set(index, 1);
    	} else {
    		hit.incrementAndGet(index);//add one
    	}
        
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
    	int total = 0;
    	for (int i = 0; i < 300; i++) {
    		if (timestamp - time.get(i) < 300) {
    			total += hit.get(i);
    		}
    	}
    	return total;
    }
}
```

