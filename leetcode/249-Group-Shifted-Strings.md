# 249. Group Shifted Strings 

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

    "abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

    For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], Return:

    [
    ["abc","bcd","xyz"],
    ["az","ba"],
    ["acef"],
    ["a","z"]
    ]
Note: For the return value, each inner list's elements must follow the lexicographic order.

## Thoughts

Use Hash function to calculate the difference between the current character and the previous character for all the characters in the string starting from index 1. 

## Solution

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class GroupShiftedString {
    public static List<List<String>> groupStrings(String[] strings) {
        List<List<String>> result = new ArrayList<>();
        HashMap<String, List<String>> stringMap = new HashMap<>();

        for(String s : strings) {
            String key = getHashKey(s);
            if(stringMap.containsKey(key)) {
                stringMap.get(key).add(s);
            } else {
                List<String> list = new ArrayList<>();
                list.add(s);
                stringMap.put(key, list);
            }
        }

        for(String key : stringMap.keySet()) {
            List<String> stringList = stringMap.get(key);
            Collections.sort(stringList);
            result.add(stringList);
        }

        return result;
    }

    private static String getHashKey(String s) {
        if(s.length() == 0) {
            return "0";
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 1; i < s.length(); i++) {
            int diff = (s.charAt(i) - s.charAt(i - 1) + 26) % 26;
            sb.append(diff);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println(groupStrings(new String[]{"abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"}));
    }
}
```