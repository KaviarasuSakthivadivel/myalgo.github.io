# 244. Shortest Word Distance II
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

    For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

    Given word1 = “coding”, word2 = “practice”, return 3. Given word1 = "makes", word2 = "coding", return 1.

## Thoughts

Design a class with a HashMap for holding all the words with the respective index in the string array. 

When searching for the shortest distance, get both the index list from the HashMap. 

## Solution 
```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class ShortestWordDistance {
    public HashMap<String, List<Integer>> wordMap;

    public ShortestWordDistance(String[] words) {
        wordMap = new HashMap<>();

        for (int i = 0 ; i < words.length; i++) {
            String word = words[i];
            List<Integer> list = wordMap.getOrDefault(word, new ArrayList<>());
            list.add(i);
            wordMap.put(word, list);
        }
    }

    public int getShortestWordDistance(String word1, String word2) {
        List<Integer> list1 = wordMap.get(word1);
        List<Integer> list2 = wordMap.get(word2);
        int i = 0, j = 0;
        int s = Integer.MAX_VALUE;

        while(i < list1.size() && j < list2.size()) {
            s = Math.min(s, Math.abs(list1.get(i) - list2.get(j)));

            if(list1.get(i) < list2.get(j)) {
                i++;
            } else {
                j++;
            }
        }
        return s;
    }

    public static void main(String[] args) {
        String[] words = new String[]{"practice", "makes", "perfect", "coding", "makes"};
        ShortestWordDistance shortestWordDistance = new ShortestWordDistance(words);
        System.out.println(shortestWordDistance.getShortestWordDistance("makes", "coding"));
    }
}
```