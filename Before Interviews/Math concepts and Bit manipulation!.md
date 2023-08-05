### Convert String to Int

```java
public static int convertStringToInt(String str) {
	int result = 0;
	int sign = 1;
	int startIndex = 0;

	// Check for a sign symbol (+/-)
	if (str.charAt(0) == '-') {
		sign = -1;
		startIndex = 1;
	} else if (str.charAt(0) == '+') {
		startIndex = 1;
	}

	for (int i = startIndex; i < str.length(); i++) {
		char c = str.charAt(i);

		// Check if the character is a valid digit
		if (c >= '0' && c <= '9') {
			// Convert character to the corresponding digit value
			int digitValue = c - '0';

			// Update the result by adding the digit
			result = result * 10 + digitValue;
		} else {
			// If any non-digit character is encountered, throw an exception or handle the error
			throw new NumberFormatException("Invalid integer string: " + str);
		}
	}

	return result * sign;
}
```

# Convert character from end to int

```java
int base = 1;
int k = 0;
while(!stack.isEmpty() && Character.isDigit(stack.peek())) {
	k = k + base * (stack.pop() - '0');
	base *= 10;
}
```

# Square of Digits

```java
private int squaresOfDigit(int n) {
	int sum = 0;
	while (n > 0) {
		sum += (n%10) * (n%10);
		n/=10;
	}
	return sum;
}
```