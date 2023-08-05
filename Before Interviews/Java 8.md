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
Arrays.sort(arr, Collections.reverseOrder());
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

