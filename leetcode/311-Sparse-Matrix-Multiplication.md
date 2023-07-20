
# 311. Sparse Matrix Multiplication

Given two [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) `mat1` of size `m x k` and `mat2` of size `k x n`, return the result of `mat1 x mat2`. You may assume that multiplication is always possible.

![[311.jpeg]]

```java
class Solution {
    public int[][] multiply(int[][] mat1, int[][] mat2) {
        int m = mat1.length;
        int k = mat1[0].length;
        int n = mat2[0].length;
        
        int[][] ans = new int[m][n];
        
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                for(int elementIdx = 0; elementIdx < k; elementIdx++) {
                    ans[i][j] += mat1[i][elementIdx] * mat2[elementIdx][j];
                }
            }
        }
        
        return ans;
    }
}
```
