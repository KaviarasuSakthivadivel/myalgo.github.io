# 271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
    string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
    }
    Machine 2 (receiver) has the function:
    vector<string> decode(string s) {
    //... your code
    return strs;
    }

    So Machine 1 does:

    string encoded_string = encode(strs);
    and Machine 2 does:

    vector<string> strs2 = decode(encoded_string);
    strs2 in Machine 2 should be the same as strs in Machine 1.

### Solution
```java
import java.util.ArrayList;
import java.util.List;

public class Codec {
    public static String encode(List<String> raw) {
        StringBuilder sb = new StringBuilder();
        for(String s : raw) {
            sb.append(s.length()).append("#").append(s);
        }
        return sb.toString();
    }

    public static List<String> decode(String encoded) {
        int k = 0;
        List<String> result = new ArrayList<>();

        while(k < encoded.length()) {
            int pound = encoded.indexOf("#", k);
            int size = Integer.parseInt(encoded.substring(k, pound));
            result.add(encoded.substring(pound + 1, pound + 1 + size));
            k = pound + 1 + size;
        }
        return result;
    }

    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("abc");
        list.add("def");
        list.add("def");
        list.add("abc");
        String encode = encode(list);
        System.out.println(encode(list));
        System.out.println(decode(encode));
    }
}
```