### DFS 4-directions

```java
int[] dirx = {0, 1, 0, -1};
int[] diry = {-1, 0, 1, 0};

for (int i = 0; i < 4; i++) {
	int r = x + dirx[i];
	int c = y + diry[i];
}
```

## DFS 4-directions 

```java
private int[] DIRECTIONS = new int[]{0, 1, 0, -1, 0}; // New method to calculate the neighbours - 4 directionally


for(int i = 0; i < 4; ++i) {
	int row = curr[0] + DIRECTIONS[i];
	int col = curr[1] + DIRECTIONS[i + 1];
}
```

