
```python

"""
Part 1
For many internet services, we need to differentiate between humans and bots. Assume we are given a sign-in attempts log with 2 columns, `time` and `IP`, where time is seconds since unix epoch and IP is a IPv4 string, and we are asked to implement a simple algorithm to detect bots.

Our algorithm is as follows: an IP is defined as a bot if it occurs equal or more than `count` times.

Function signature in python
def find_bot(log: str, count) -> list[str]:
...
With the following sample file (given to you as a string),
ts,IP
2,52.0.1.2
3,23.5.0.9
3,23.5.0.9
3,23.5.0.9
3,52.0.1.2
5,52.0.1.7
5,1.1.2.2

find_bot(log, count=2) should return [52.0.1.2, 23.5.0.9]

**

Part 2
With the help of data scientists, we have improved our algorithm!
Now a bot is defined as any IP that occurs equal or more than `count` times within `window` seconds. Also, instead of a log file, we are a service and have to answer live queries;

  
in python code
class BotIpService:
	def __init__(self, count, window_sec):
	...
	
	def is_bot(self, ts, ip) -> bool:
	...

As a concrete example,

svc = BotIpService(count=3, window_sec=3)
# assume current time is 0
svc.is_bot(0, "127.0.0.1") returns False
# assume current time is 1
svc.is_bot(1, "127.0.0.1") returns False
# assume current time is 1

svc.is_bot(1, "127.0.0.1") returns True
# assume current time is 4
svc.is_bot(4, "9.9.9.9") returns False
# assume current time is 4
svc.is_bot(4, "127.0.0.1") returns False
# assume current time is 5
svc.is_bot(5, "127.0.0.1") returns False

A few things to notice
1) the window is left exclusive and right inclusive; that is, (] in math notation; ex if current time is 5 and window is 3, the window is [3, 4, 5]

2) our service only cares about the window relative to `ts`, so a positive label for an IP might become negative
```

This is what I did in the interview. 
``
```java

import java.io.*;
import java.util.*;
// import com.fasterxml.jackson.databind.ObjectMapper;
// import com.fasterxml.jackson.core.JsonProcessingException;

// Main class should be named 'Solution' and should not be public.
class Solution {
    
    private static void findBot(List<String> logs, int count) {
        HashMap<String, Integer> ipFreqMap = new HashMap<>();
        
        for(String log : logs) {
            String[] split = log.split(",");
            String ip = split[1];
            
            ipFreqMap.put(ip, ipFreqMap.getOrDefault(ip, 0) + 1);
        }
        
        LinkedList<String> botsIp = new LinkedList<>();
        for(Map.Entry<String, Integer> entry : ipFreqMap.entrySet()) {
            if(entry.getValue() >= count) {
                botsIp.add(entry.getKey());
            }
        }
        
        System.out.println(botsIp);
    }
    
    class CurrentTimeUtil {
        private static int currentTime;
    }
    
    static class BotIpService {
        private int count;
        private int windowSize;
        private HashMap<String, LinkedList<Integer>> ipFreqMap;
         
        public BotIpService(int count, int windowSize) {
            this.count = count;
            this.windowSize = windowSize;
            this.ipFreqMap = new HashMap<>();
        }
         
        private boolean isBot(int currentTime, String ipAddr) {
            boolean isBot = false;
            
            ipFreqMap.computeIfAbsent(ipAddr, l-> new LinkedList<>()).add(currentTime);
            if(ipFreqMap.size() >= count) {
                isBot = true;
            }
            int diff = currentTime - windowSize;
            while(!ipFreqMap.get(ipAddr).isEmpty() && diff > 0) {
                diff--;
	             ipFreqMap.get(ipAddr).removeFirst();
            // }
            return isBot;
        }
     }
    
    public static void main(String[] args) {
        System.out.println("Hello, World");
        
        List<String> logs = Arrays.asList("2,52.0.1.2", "3,23.5.0.9", "3,23.5.0.9", "3,23.5.0.9", "3,52.0.1.2", "5,52.0.1.7", "5,1.1.2.2");

        findBot(logs, 2);
        
        BotIpService ipService = new BotIpService(3, 3);
        System.out.println(ipService.isBot(0, "127.0.0.1"));
        System.out.println(ipService.isBot(1, "127.0.0.1"));
        System.out.println(ipService.isBot(1, "127.0.0.1"));
        
        System.out.println(ipService.isBot(4, "9.9.9.9"));
        System.out.println(ipService.isBot(4, "127.0.0.1"));
        System.out.println(ipService.isBot(5, "127.0.0.1"));
        /*
        # assume current time is 0
svc.is_bot(0, "127.0.0.1") returns False
# assume current time is 1
svc.is_bot(1, "127.0.0.1") returns False
# assume current time is 1
svc.is_bot(1, "127.0.0.1") returns True
 
# assume current time is 4
svc.is_bot(4, "9.9.9.9") returns False
# assume current time is 4
svc.is_bot(4, "127.0.0.1") returns False
# assume current time is 5
svc.is_bot(5, "127.0.0.1") returns False
        */
        
    }
}


```


### Actual Answer

```java
import java.util.Arrays;  
import java.util.HashMap;  
import java.util.LinkedList;  
import java.util.List;  
import java.util.Map;  
  
class BotIpService {  
    private int count;  
    private int windowSize;  
    private HashMap<String, LinkedList<Integer>> ipFreqMap;  
  
    public BotIpService(int count, int windowSize) {  
        this.count = count;  
        this.windowSize = windowSize;  
        this.ipFreqMap = new HashMap<>();  
    }  
  
    private boolean isBot(int currentTime, String ipAddr) {  
        while(!ipFreqMap.getOrDefault(ipAddr, new LinkedList<>()).isEmpty()) {  
            int diff = currentTime - ipFreqMap.get(ipAddr).getFirst();  
            if(diff >= windowSize) {  
                ipFreqMap.get(ipAddr).removeFirst();  
            } else {  
                break;  
            }  
        }  
        ipFreqMap.computeIfAbsent(ipAddr, l-> new LinkedList<>()).add(currentTime);  
        return ipFreqMap.get(ipAddr).size() >= count;  
    }  
  
    public static void main(String[] args) {  
        List<String> logs = Arrays.asList("2,52.0.1.2", "3,23.5.0.9", "3,23.5.0.9", "3,23.5.0.9", "3,52.0.1.2", "5,52.0.1.7", "5,1.1.2.2");  
  
        findBot(logs, 2);  
  
        BotIpService ipService = new BotIpService(3, 3);  
        System.out.println(ipService.isBot(0, "127.0.0.1"));  
        System.out.println(ipService.isBot(1, "127.0.0.1"));  
        System.out.println(ipService.isBot(1, "127.0.0.1"));  
  
        System.out.println(ipService.isBot(4, "9.9.9.9"));  
        System.out.println(ipService.isBot(4, "127.0.0.1"));  
        System.out.println(ipService.isBot(5, "127.0.0.1"));  
    }  
  
    private static void findBot(List<String> logs, int count) {  
        HashMap<String, Integer> ipFreqMap = new HashMap<>();  
  
        for(String log : logs) {  
            String[] split = log.split(",");  
            String ip = split[1];  
  
            ipFreqMap.put(ip, ipFreqMap.getOrDefault(ip, 0) + 1);  
        }  
  
        LinkedList<String> botsIp = new LinkedList<>();  
        for(Map.Entry<String, Integer> entry : ipFreqMap.entrySet()) {  
            if(entry.getValue() >= count) {  
                botsIp.add(entry.getKey());  
            }  
        }  
  
        System.out.println(botsIp);  
    }  
}
```