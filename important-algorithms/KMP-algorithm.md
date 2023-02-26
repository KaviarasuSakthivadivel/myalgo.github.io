# KMP algorithm

**Tricky party:**
    
    len = lps[len-1];

Consider the example "ababe......ababc", i is index of 'c', len==4. The longest prefix suffix is "abab", when pat[i]!=pat[len], we get new prefix "ababe" and suffix "ababc", which are not equal. 

This means we can't increment length of lps based on current lps "abab" with len==4. We may want to increment it based on the longest prefix suffix with length < len==4, which by definition is lps of "abab". So we set len to lps[len-1], which is 2, now the lps is "ab". Then check pat[i]==pat[len] again due to the while loop, which is also the reason why we do not increment i here. The iteration of i terminate until len==0 (didn't find lps ends with pat[i]) or found a lps ends with pat[i].


```java
void computeLPSArray(char[] pat, int M, int[] lps) {
    int len = 0;  // lenght of the previous longest prefix suffix
    int i;

    lps[0] = 0; // lps[0] is always 0
    i = 1;

    // the loop calculates lps[i] for i = 1 to M-1
    while (i < M) {
        //example "abababca" and i==5, len==3. The longest prefix suffix is "aba", when pat[i]==pat[len],
        //we get new prefix "abab" and new suffix "abab", so increase length of  current lps by 1 and go to next iteration. 
        if (pat[i] == pat[len]) {
            len++;
            lps[i] = len;
            i++;
        }
        else { // (pat[i] != pat[len]) 
            if (len != 0) {
                len = lps[len-1];
                //This is tricky. Consider the example "ababe......ababc", i is index of 'c', len==4. The longest prefix suffix is "abab",
                //when pat[i]!=pat[len], we get new prefix "ababe" and suffix "ababc", which are not equal. 
                //This means we can't increment length of lps based on current lps "abab" with len==4. We may want to increment it based on
                //the longest prefix suffix with length < len==4, which by definition is lps of "abab". So we set len to lps[len-1],
                //which is 2, now the lps is "ab". Then check pat[i]==pat[len] again due to the while loop, which is also the reason
                //why we do not increment i here. The iteration of i terminate until len==0 (didn't find lps ends with pat[i]) or found
                //a lps ends with pat[i].
            }
            else { // if (len == 0)
                lps[i] = 0; // there isn't any lps ends with pat[i], so set lps[i] = 0 and go to next iteration.
                i++;
            }
        }
    }
}  
```

### KMP search
```java
void KMPSearch(String pat, String txt) {
    int M = pat.length();
    int N = txt.length();

    // create lps[] that will hold the longest
    // prefix suffix values for pattern
    int lps[] = new int[M];
    int j = 0; // index for pat[]

    // Preprocess the pattern (calculate lps[]
    // array)
    computeLPSArray(pat, M, lps);

    int i = 0; // index for txt[]
    while (i < N) {
        if (pat.charAt(j) == txt.charAt(i)) {
            j++;
            i++;
        }
        if (j == M) {
            System.out.println("Found pattern at index " + (i - j));
            j = lps[j - 1];
        }

        // mismatch after j matches
        else if (i < N && pat.charAt(j) != txt.charAt(i)) {
            // Do not match lps[0..lps[j-1]] characters,
            // they will match anyway
            if (j != 0)
                j = lps[j - 1];
            else
                i = i + 1;
        }
    }
}
```