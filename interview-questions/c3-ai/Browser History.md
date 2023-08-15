```java
import java.util.*;
import java.io.*;

class Main {
    private List<String> history;
    private int last, current;

    public Main() {
        history = new ArrayList<>();
        last = 0;
        current = -1;
    }

    private void visit(String url) {
        current++;
        if(current < history.size()) {
            history.set(current, url);
        } else {
            history.add(url);
        }
        last = current;

        System.out.println(history);
        System.out.println(current + " : " + last);
    }

    private String go(int steps) {
        if(steps < 0) { // going backward
            current = Math.max(0, current + steps);
            return history.get(current);
        } else { // going forward
            current = Math.min(last, current + steps);
            return history.get(current);
        }
    }

    public static void main (String[] args) {
        Main main = new Main();
        main.visit("google.com");
        main.visit("c3.ai");
        main.visit("c3.ai/news");
        System.out.println(main.go(-2));
        System.out.println(main.go(1));
        main.visit("c3.ai/apps");
        main.visit("c3.ai/apps/genAI");
        System.out.println(main.go(-2));
    }

}
```