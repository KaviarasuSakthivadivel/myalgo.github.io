
[How do I get my email working with my phone, 
How do I get my email working with my iphone
How do I get my email working with my android, 
How do I get my outlook working with my phone, 
How do I get my outlook working with my iphone,
How do I get my outlook working with my android]



You can assume all strings contains only letters [a-z]. Part 1: Synsets will only contain one word. Example 1: S - "How do I get my email working with my phone" B - ['email|outlook', 'iphone|phone|android' ] "How do I get my email working with my android" "How do I det my email working with my iphone" "How do I get my email working with my phone", "How do I get my outlook working with my android" "How do i get my outlook working with my iphone" "How do I get my outlook working with my phone"


```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

public class Synset {

    private static void backtrack(StringBuilder s, int idx, List<String> wordsToReplace, HashMap<String, HashSet<String>> dict, List<String> result) {
        result.add(s.toString());

        for(int i = idx; i < wordsToReplace.size(); i++) {
            String currentWord = wordsToReplace.get(i);
            HashSet<String> possibleWordsToReplace = dict.getOrDefault(currentWord, new HashSet<>());
            for(String nextWord : possibleWordsToReplace) {
                String s1 = s.toString().replaceAll(currentWord, nextWord);
                backtrack(new StringBuilder(s1), i + 1, wordsToReplace, dict, result);
            }
        }
    }

    private static List<String> replaceSynset(String S, String[] B) {
        List<String> results = new ArrayList<>();
        HashMap<String, HashSet<String>> dict = new HashMap<>();
        List<String> wordsToReplace = new ArrayList<>();

        for(String pattern : B) {
            String[] words = pattern.split("\\|");

            for(String word : words) {
                if(S.contains(word)) {
                    dict.putIfAbsent(word, new HashSet<>());
                    wordsToReplace.add(word);

                    for(String wordToAdd : words) {
                        if(!wordToAdd.equals(word)) {
                            dict.get(word).add(wordToAdd);
                        }
                    }
                    break;
                }
            }
        }

//        System.out.println(dict);
        backtrack(new StringBuilder(S), 0, wordsToReplace, dict, results);

        return results;
    }

    public static void main(String[] args) {
        String s = "How do I get my email working with my phone";
        String[] B = new String[]{"email|outlook", "iphone|phone|android"};

        System.out.println(replaceSynset(s, B));
    }
}

```


```
[How do I get my email working with my phone, 
How do I get my email working with my iphone,
How do I get my outlook working with my phone, 
How do I get my outlook working with my iphone, 
How can I get my outlook working with my iphone, 
How can I get my outlook working with my phone, 
How can I get my email working with my iphone, 
How can I get my email working with my phone]
```