# 681. Next Closest Time

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.


    Example 1:

    Input: time = "19:34"
    Output: "19:39"
    Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
    It is not 19:33, because this occurs 23 hours and 59 minutes later.
    Example 2:

    Input: time = "23:59"
    Output: "22:22"
    Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
    It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

## Solution

### Approach 

1. Convert the given time into minutes. 
2. Keep a set to maintain the given digits in the given time. 
3. Run a infinite loop till you find the next time. To Handle the case 11:59, take a modulo, ie, ```(minutes + 1) % (24 * 60)``` so that it can wrap around to 00:00. 


```java
class Solution {
    private final int TOTAL_MINUTES = 24 * 60;
    
    public String nextClosestTime(String time) {
        
        // Convert the string to minutes. 
        int minutes = Integer.parseInt(time.substring(0, 2)) * 60;
        minutes += Integer.parseInt(time.substring(3));
        
        // Set to check if the next generating time is there in the digits
        HashSet<Integer> digitSet = new HashSet<>();
        for(char ch : time.toCharArray()) {
            digitSet.add(ch - '0');
        }
        
        while(true) {    
            // Edge case to handle 11:59, we need to wrap around to 00:00
            minutes = (minutes + 1) % (TOTAL_MINUTES);
            
            int[] nextTime = new int[]{
                minutes / 60 / 10, 
                minutes / 60 % 10, 
                minutes % 60 / 10,
                minutes % 60 % 10
            };
            
            boolean isValid = true;
            
            for(int digit : nextTime) {
                if(!digitSet.contains(digit)) {
                    isValid = false;
                }
            }
            
            if(isValid) {
                return String.format("%02d:%02d", minutes / 60, minutes % 60);
            }
        }
    }
}
```