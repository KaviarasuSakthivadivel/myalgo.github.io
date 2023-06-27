
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