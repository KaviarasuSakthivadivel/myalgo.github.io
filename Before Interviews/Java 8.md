# Streams 

[[1029. Two City Scheduling]]

# Convert int array to array list using Streams

```java
List<Integer> arrayList = Arrays.stream(nums).boxed().collect(Collectors.toList());
```


# Convert Array list to int array using Streams

```java
res.stream().mapToInt(i->i).toArray();
```

# Sort the array in reverse

```java
Collections.sort(arr, Collections.reverseOrder());
```

# Sort the Object based on a field

```java
Interval[] intervals = new Intervals[]{};
Arrays.sort(intervals, Comparator.comparingInt((Interval i) -> i.start));
```

# Convert Array List to int[]

```java
return list.toArray(new int[list.size()][]);
```

# Sort array by frequency

```java
public int[] frequencySort(int[] nums) {
	HashMap<Integer, Integer> freqMap = new HashMap<>();

	for(int num : nums) {
		freqMap.put(num, freqMap.getOrDefault( num, 0) + 1);
	}

	return Arrays.stream(nums)
					.boxed()
					.sorted((a, b) -> freqMap.get(a) != freqMap.get(b) ? freqMap.get(a) - freqMap.get(b) : b - a)
					.mapToInt(n -> n).toArray();
}
```


# Filter function use cases

## Get occurences of a particular character and cheching

```java
if(queryIP.chars().filter(ch -> ch == '.').count() == 3) {}
```

