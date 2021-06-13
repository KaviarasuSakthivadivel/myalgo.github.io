# 269. Alien Dictionary
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1: Given the following words in dictionary,

    [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
    ]
The correct order is: "wertf".

Example 2: Given the following words in dictionary,

    [
    "z",
    "x"
    ]
The correct order is: "zx".

Example 3: Given the following words in dictionary,

    [
    "z",
    "x",
    "z"
    ]
The order is invalid, so return "".

Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

### Thoughts
<u>**In normal dictionary**</u> If the words are given in lexicographically sorted order like `{"azd", "zad"}`, we can compare the first different character in the string to know which character comes before which one. Here, **a** comes before **z**. 

<u>**In Alien Dictionary**</u>
    
    [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
    ]

Compare **wrt** | **wrf**, first different character here is t and f, so, we can deduct `t` comes before `f`.

Compare **wrf** | **er**,  `w` is before `e`.

Compare **er** | **ett**, `r` is before `t`

Compare **ett** | **rftt**, `e` is before `r`

#### Algorithm
We try to build an order that fullfill the relationships given. Here the relationship is the order of two characters. ** a -> b ** We can use the directed graph to represent the relationship. 

Use Topological sorting of the letters. Topological sorting is possible if and only if the graph has no directed cycles, if there are cycles, then we return the empty string.


### Solution
```java
import java.util.*;

public class AlienDictionary {
    public static String alienOrder(String[] words) {
        Map<Character, Set<Character>> graph = new HashMap<>();
        int[] inDegree = new int[26];
        buildGraph(graph, words, inDegree);
        return bfs(graph, words, inDegree);
    }

    private static String bfs(Map<Character, Set<Character>> graph, String[] words, int[] inDegree) {
        StringBuilder sb = new StringBuilder();
        Queue<Character> queue = new LinkedList<>();
        for(char c : graph.keySet()) {
            if (inDegree[c - 'a'] == 0) {
                queue.offer(c);
            }
        }
        while(!queue.isEmpty()) {
            Character u = queue.poll();
            sb.append(u);
            for(Character ch : graph.get(u)) {
                if(--inDegree[ch - 'a'] == 0) {
                    queue.add(ch);
                }
            }
        }
        return graph.size() == sb.length() ? sb.toString() : "";
    }

    private static void buildGraph(Map<Character, Set<Character>> graph, String[] words, int[] inDegree) {
        for(String word : words) {
            for(Character ch : word.toCharArray()) {
                graph.putIfAbsent(ch, new HashSet<>());
            }
        }
        for(int i = 1 ; i < words.length; i++) {
            String first = words[i - 1];
            String second = words[i];
            int len = Math.min(first.length(), second.length());

            for(int j = 0; j < len; j++) {
                char out = first.charAt(j);
                char in = second.charAt(j);
                if(out != in) {
                    if(!graph.get(out).contains(in)) {
                        graph.get(out).add(in);
                        inDegree[in - 'a']++;
                    }
                    break;
                    // We need to consider only the first different character, so breaking the loop here.
                }
            }
        }

    }

    public static void main(String[] args) {
        String[] words = new String[]{"wrt", "wrf", "er", "ett", "rftt"};
        System.out.println(alienOrder(words));
    }
}
```