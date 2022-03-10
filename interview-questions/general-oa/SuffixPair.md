# Suffix Pairs

Given an array of Strings, your task is to find the number of pairs which one is a suffix of other string

    strings = ["cba", "a", "a","b", "ba", "ca"]
    output = 
    [cba, a] // a is suffix in cb`a`
    [cba, a]
    [a, a] 
    [ba, a] // a is suffix in b`a`
    [ca, a]
    [cba, ba]
    [a, ba]
    [a, ca]

### Solution
Build a trie and on loop, check the string if it's end of that word, add the count to the result. Keep freq count in the trie node to handle the duplicates. 

```java
package com.ub.algorithms.interviews;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

public class SuffixPairs {
    TrieNode root;
    public SuffixPairs() {
        root = new TrieNode();
    }
    private int buildTreeAndGetCount(String word) {
        TrieNode current = root;
        int count = 0;
        for(Character ch : word.toCharArray()) {
            if(!current.children.containsKey(ch)) {
                current.children.put(ch, new TrieNode());
            }
            
            current = current.children.get(ch);
            if(current.isEnd) {
                count += current.freq;
            }
        }
        current.isEnd = true;
        current.freq++;

        return count;
    }

    public static void main(String[] args) {
        SuffixPairs suffixPairs = new SuffixPairs();
        List<String> strings = Arrays.asList("cba", "a", "a","b", "ba", "ca");
        strings.sort(Comparator.comparingInt(String::length));
        int pairsCount = 0;
        for(String s : strings) {

            pairsCount += suffixPairs.buildTreeAndGetCount(new StringBuilder(s).reverse().toString());
        }
        System.out.println(pairsCount);
    }
}

class TrieNode {
    HashMap<Character, TrieNode> children;
    boolean isEnd;
    int freq;

    public TrieNode() {
        children = new HashMap<>();
        isEnd = false;
        freq = 0;
    }
}
```
