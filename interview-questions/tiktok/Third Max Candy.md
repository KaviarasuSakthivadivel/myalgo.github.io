The child with third maximum candies
There is a list of children, each one has some candies in hand. Please find the third distinct maximum candies. 
If there is no such number, please return the max candies in children's hands.
Input: nums = [3,2,1]
Output: 1
Input: nums = [1,2]
Output: 2
Input: nums = [4,3,3,2]
Output: 2

[414. Third Maximum Number](https://leetcode.com/problems/third-maximum-number/)

## My Solution in the interview

```java
import java.util.HashSet;
import java.util.PriorityQueue;

public class ThirdMax {

    // O(n log3)
    private static int getThirdMax(int[] arr) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        HashSet<Integer> set = new HashSet<>();

        for(int curr : arr) {
            if(!set.contains(curr)) {
                if(queue.size() >= 3) {
                    if(queue.peek() < curr) {
                        queue.remove();
                        queue.add(curr);
                        set.add(curr);
                    }
                } else {
                    queue.add(curr);
                    set.add(curr);
                }
            }
            System.out.println(queue);
        }

        return !queue.isEmpty() ? queue.poll() : -1;
    }


    public static void main(String[] args) {
        System.out.println(getThirdMax(new int[]{4, 5, 5, 6, 7, 9 }));
    }

}
```

## Efficient 

We can solve this without using any queue itself. 

```java
public class ThirdMaxCandies {
    public static int thirdMax(int[] nums) {
        Integer max1 = null;
        Integer max2 = null;
        Integer max3 = null;

        for (Integer num : nums) {
            if (num.equals(max1) || num.equals(max2) || num.equals(max3)) {
                continue;
            }

            if (max1 == null || num > max1) {
                max3 = max2;
                max2 = max1;
                max1 = num;
            } else if (max2 == null || num > max2) {
                max3 = max2;
                max2 = num;
            } else if (max3 == null || num > max3) {
                max3 = num;
            }
        }

        return (max3 == null) ? max1 : max3;
    }

    public static void main(String[] args) {
        int[] nums1 = {3, 2, 1};
        int[] nums2 = {1, 2};
        int[] nums3 = {4, 3, 3, 2};

        System.out.println(thirdMax(nums1));  // Output: 1
        System.out.println(thirdMax(nums2));  // Output: 2
        System.out.println(thirdMax(nums3));  // Output: 2
    }
}
```

## Another Solution

```java
public int thirdMax(int[] nums) {
	HashSet<Integer> seen = new HashSet<>();
	PriorityQueue<Integer> queue = new PriorityQueue<>();

	for(int num : nums) {
		if(seen.contains(num)) {
			continue;
		}

		seen.add(num);
		if(queue.size() == 3) {
			if(queue.peek() < num) {
				queue.poll();
				queue.add(num);
			}
		} else {
			queue.add(num);
		}
	}

	if(queue.size() == 3) {
		return queue.peek();
	} else {
		int max = -1;
		while(!queue.isEmpty()) {
			max = Math.max(max, queue.poll());
		}
		return max;
	}
}

public int thirdMaxUsingSet(int[] nums) {
	
	Set<Integer> set = new HashSet<>();
	
	for(int num : nums) {
		set.add(num);
		
		if(set.size() > 3) {
			set.remove(Collections.min(set));
		}
	}
	
	if(set.size() == 3) {
		return Collections.min(set);
	}
	
	return Collections.max(set);
}
```