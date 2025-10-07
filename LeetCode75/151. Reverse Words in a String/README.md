# Reverse Words in a String

## Problem Link
[LeetCode - Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

## Problem Topics
Strings, Two Pointers, Parsing, Stack (conceptually), String Manipulation

## Problem Description
Given an input string `s`, reverse the order of the words.  
A word is defined as a sequence of non-space characters.  
The words in `s` are separated by at least one space.  
Return a string of the words in reverse order concatenated by a single space.  

**Note:** Extra spaces before or after words should be trimmed, and multiple spaces between words should be reduced to one.

## Example Input / Output

**Example 1:**  
Input: `s = "the sky is blue"`  
Output: `"blue is sky the"`

**Example 2:**  
Input: `s = "  hello world  "`  
Output: `"world hello"`

**Example 3:**  
Input: `s = "a good   example"`  
Output: `"example good a"`

## Pseudocode
1. Initialize an empty list `sent` to store words.  
2. Iterate through the string, skipping leading spaces.  
3. For each word:
   - Collect characters until a space or end of string is found.  
   - Append the word to `sent`.  
4. Reverse the `sent` list.  
5. Join the reversed words with a single space and return the result.  

## My Java Solution Approach
- **Logic:** The Java approach manually parses the string, extracts words, stores them in a list, and then reverses that list before joining it back into a single string.  

### **Code Explanation**
1. `List<String> sent = new ArrayList<>();` → creates a dynamic list to hold words.  
2. `while (i < leng && s.charAt(i) == ' ') i++;` → skips leading spaces.  
3. For each word:
   - Use `StringBuilder word = new StringBuilder();` to build the current word.  
   - Keep appending characters until a space is found.  
   - Add the completed word to `sent` using `sent.add(word.toString())`.  
4. Once all words are collected, use `Collections.reverse(sent)` to reverse the order of words.  
5. Finally, `String.join(" ", sent)` joins all reversed words with a single space and returns the result.

### **New Methods / Functions / Libraries Used**
- `ArrayList`: a resizable list in Java to store elements dynamically.  
- `Collections.reverse()`: reverses the order of elements in a list in-place.  
- `String.join(delimiter, list)`: joins elements of a list into a single string with the given delimiter.  
- `StringBuilder`: an efficient mutable sequence of characters used for building strings in loops.  

## My Python Solution Approach
- **Logic:** Similar to Java — it manually parses through the string, identifies words, appends them to a list, reverses the list, and joins them into a single space-separated string.

### **Code Explanation**
1. `sent = []` → creates an empty list to store extracted words.  
2. `while i < n and s[i] == " ": i += 1` → skips any leading spaces.  
3. For each word:
   - Use `word = []` → a temporary list to store characters of the current word.  
   - Append each non-space character using `word.append(s[i])`.  
   - When a space is reached, join the collected characters with `"".join(word)` and add to `sent`.  
4. After processing the full string, `reversed(sent)` is used to reverse the list of words.  
5. `" ".join(reversed(sent))` → joins reversed words with a single space to produce the final output.

### **New Methods / Functions / Libraries Used**
- `"".join(list)`: concatenates elements of a list into a single string.  
- `reversed(iterable)`: returns a reversed iterator of the given sequence.  
- `" ".join(...)`: joins the reversed words with single spaces efficiently.  

## Complexities of My Approach
- **Time Complexity:** `O(n)` — every character in the string is processed exactly once.  
- **Space Complexity:** `O(n)` — for storing extracted words and reversed order.  

## Self Learning
- Improved understanding of manual string parsing without built-in split functions.  
- Reinforced the concept of reversing collections and string concatenation in both Java and Python.  
- Practiced managing character indices carefully for whitespace handling.  

## Can It Be Improved?
- Yes. Instead of manually parsing, you can use built-in split and reverse operations:  
  - **Java:**  
    ```java
    String[] words = s.trim().split("\\s+");
    Collections.reverse(Arrays.asList(words));
    return String.join(" ", words);
    ```
  - **Python:**  
    ```python
    return " ".join(reversed(s.split()))
    ```
  - This shortens code and leverages efficient library implementations while maintaining `O(n)` complexity.
