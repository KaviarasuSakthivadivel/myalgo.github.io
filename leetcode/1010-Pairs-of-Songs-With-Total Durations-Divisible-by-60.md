# 1010. Pairs of Songs With Total Durations Divisible by 60

You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.


    Input: time = [30,20,150,100,40]
    Output: 3
    Explanation: Three pairs have a total duration divisible by 60:
    (time[0] = 30, time[2] = 150): total duration 180
    (time[1] = 20, time[3] = 100): total duration 120
    (time[1] = 20, time[4] = 40): total duration 60


### Solution 
Indeed, this looks like a variant of 2 sum, the only difference being that we are concerned about the modulo sum here instead of the absolute sum. Here's my take:

1.Distribute the numbers in buckets 0-59 i.e num % 60.
2.Bucket x's complimentary is bucket 60-x. For e.g bucket 20's complimentary is bucket 40. This means that adding up the number's in bucket 20 and bucket 40 would definitely give sum which is divisible by 60. For e.g.

bucket no.20=[20,80,140]
bucket no.40=[40,100,160]

    (20 + 40) % 60 == 0
    (20 + 100) % 60 == 0
    (20 + 160) % 60 == 0
    ...
    ...
    (140 + 160) % 60 == 0

3.With the above point in mind, whenever you are going to add a number in bucket no. x, check how many items are there in its complimentary bucket no. 60-x because all those items would form valid pairs with the current item to yield a sum divisible by 60. So add the number of items in the complimentary bucket to the running total of the number of valid pairs found out till now.

```java

class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int[] arr = new int[60];
        int ans = 0;
        for(int t : time) {
            int r = t % 60;
            ans = ans + arr[(60 - r) % 60];
            arr[r]++;
        }
        return ans;
    }
}

```