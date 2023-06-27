### Find the number of zeroes

Given an array of 1s and 0s which has all 1s first followed by all 0s. Find the number of 0s. Count the number of zeroes in the given array.


```java
public class CountZeroes {

    private static int binarySearch(int[] arr, int target, boolean firstOccurrence) {
        int index = -1;

        int left = 0, right = arr.length - 1;
        while(left <= right) {
            int mid = left + (right - left) / 2;
            if(arr[mid] == target) {
                index = mid;

                if(firstOccurrence) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else if(arr[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return index;
    }

    private static void countZero(int[] arr) {
        int left = 0, right = arr.length - 1;
        int startingZeroIndex = -1;
        while(left <= right) {
            int mid = left + (right - left) / 2;

            if(mid == 0 || (arr[mid] == 0 && arr[mid - 1] == 1)) {
                startingZeroIndex = mid;
                break;
            } else if(arr[mid] == 1) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        if(startingZeroIndex != -1) {
            System.out.println(arr.length - startingZeroIndex);
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[] {1, 2, 3, 5, 5, 5, 7, 8, 10};
        System.out.println(binarySearch(arr, 5, true));

        int[] zeroArr = new int[]{1,1,1,1,1,1,0,0,0,0,0,0};
//        System.out.println(binarySearch(arr, 0, true));
        countZero(zeroArr);
    }
}

```