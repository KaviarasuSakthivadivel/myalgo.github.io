### How does String tokenizer work in Java?

In Java, the StringTokenizer class is used to break a string into tokens (or smaller pieces) based on a delimiter. The delimiter is typically a character or a set of characters that separate the tokens.

Here's an example of how to use StringTokenizer in Java:

```java
String input = "Hello, world! How are you today?";
String delimiter = " ,!?"; // Delimiters are space, comma, exclamation mark, and question mark

StringTokenizer tokenizer = new StringTokenizer(input, delimiter);

while (tokenizer.hasMoreTokens()) {
    String token = tokenizer.nextToken();
    System.out.println(token);
}
```

This code creates a StringTokenizer object with an input string "Hello, world! How are you today?" and a set of delimiters consisting of space, comma, exclamation mark, and question mark. The while loop then iterates through each token in the input string and prints it out.

To create your own StringTokenizer class in Java, you can start by defining a constructor that takes an input string and a set of delimiters as parameters. You can then create a nextToken() method that returns the next token in the input string and a hasMoreTokens() method that returns true if there are more tokens to be processed. Finally, you can define a reset() method that resets the tokenizer to the beginning of the input string.

Here's an example implementation of a custom StringTokenizer class in Java:


### Using Iterator

```java
import java.util.Iterator;

public class MyStringTokenizer implements Iterator<String> {

    private final String text;
    private final String delimiter;
    private int currentIndex;

    public MyStringTokenizer(String text, String delimiter) {
        this.text = text;
        this.delimiter = delimiter;
        this.currentIndex = 0;
    }

    @Override
    public boolean hasNext() {
        return this.currentIndex < text.length();
    }

    @Override
    public String next() {
        if(hasNext()) {
            int delimiterIndex = text.indexOf(delimiter, currentIndex);

            if(delimiterIndex == -1) { // delimiter is not found anymore, so return the remaining string
                String token = text.substring(this.currentIndex);
                this.currentIndex = text.length();
                return token;
            }

            // save the current index as delimiter index + delimiter size, to skip to the next token starting.
            // return the substring from current index to delimiter index
            String token = text.substring(currentIndex, delimiterIndex);
            currentIndex = delimiterIndex + delimiter.length();
            return token;
        }
        return null;
    }

    public static void main(String[] args) {
        MyStringTokenizer tokenizer = new MyStringTokenizer("This is India", " ");

        while(tokenizer.hasNext()) {
            System.out.println(tokenizer.next());
        }
    }
}
```
