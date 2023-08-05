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

### Thoughts

Use Hash function to calculate the difference between the current character and the previous character for all the characters in the string starting from index 1. 

### Solution

```java
class Solution {
    // Designing the hash key such that, collision is there and all the shifted string goes to the same bucket. 
    private char shiftChar(char ch, int shift) {
        return (char) ((ch - shift + 26) % 26);
    }
    
    private String _hash(String str) {
        int shift = (int) str.charAt(0);
        StringBuilder sb = new StringBuilder();
        for(char ch : str.toCharArray()) {
            char shiftedCh = shiftChar(ch, shift);
            sb.append(shiftedCh);
        }
        
        return sb.toString();
    }
    
    public List<List<String>> groupStrings(String[] strings) {
        HashMap<String, List<String>> map = new HashMap<>();
        
        for(String str : strings) {
            String hashKey = _hash(str);
            map.computeIfAbsent(hashKey, l -> new ArrayList<>()).add(str);
        }
        
        return new ArrayList(map.values());
    }
}
```