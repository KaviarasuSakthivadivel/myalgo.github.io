```java
import java.util.Arrays;

public class Histogram {

    private double[] bins;
    private boolean evenlySpacedBuckets;
    private int[] freqCounter;

    public Histogram(double[] bins, boolean evenlySpacedBuckets) {
        this.bins = bins;
        this.evenlySpacedBuckets = evenlySpacedBuckets;
        freqCounter = new int[bins.length - 1];
    }

    public void addValue(double num) {
        // modified binary search to index of the range that num is in
        System.out.println(Arrays.toString(bins));
        System.out.println(num);
        int idx = Arrays.binarySearch(bins, 0, bins.length - 1, num);
        System.out.println(idx);
        if(idx >= 0) {
            freqCounter[idx]++;
        } else {
            int tempIdx = (idx * -1) - 2;
            System.out.println(tempIdx);
            freqCounter[tempIdx]++;
        }
    }

    public void addValue0(double num) {
        // modified binary search to index of the range that num is in
        int idx = binarySearch(bins, 0, bins.length - 1, num);
        if(idx >= 0) {
            freqCounter[idx]++;
        }
    }

    private int binarySearch(double[] bins, int left, int right, double num) {
        while(left <= right) {
            int mid = left + (right - left) / 2;

            if(num == bins[mid]) {
                return mid;
            } else if(num > bins[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return right;
    }

    public int[] getFrequencies() {
        return freqCounter;
    }

    public static void main (String[] args) {
        double[] bins = new double[]{1L, 1.5, 1.8, 2.3, 4};
        Histogram histogram = new Histogram(bins, false);

        double[] values = new double[]{1.2, 3.0, 2.0, 1.3, 3.4, 2.1, 1.6};
        for(double num : values) {
            histogram.addValue0(num);
        }

        System.out.println(Arrays.toString(histogram.getFrequencies()));
    }

    // Method 1 - HashMap<Pair<Long, Long>, Integer> (<range>, frequencies) //
    // 2 - addvalue(num) - bins - [] freq - [0 - bins.length - 1] // O(N)
    // since sorted, binary search - bucket which? O(KlogN)
}
```