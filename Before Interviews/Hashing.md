[[249-Group-Shifted-Strings]]

```java
private char shiftChar(char ch, int shift) {
	return (char) ((ch - shift + 26) % 26);
}
```

