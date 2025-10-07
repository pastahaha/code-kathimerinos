# Reverse Vowels of a String

## Problem Link
[LeetCode - Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

## Problem Topics
Two Pointers, String Manipulation

## Problem Description
Given a string `s`, reverse only all the vowels in the string and return it.  
The vowels are `'a', 'e', 'i', 'o', 'u'`, and they can appear in either lowercase or uppercase.

## Example Input / Output
**Example 1:**  
Input: `s = "hello"`  
Output: `"holle"`  

**Example 2:**  
Input: `s = "leetcode"`  
Output: `"leotcede"`  

---

## Pseudocode
1. Define a set of vowels (both uppercase and lowercase).  
2. Convert the string into a list of characters for in-place swapping.  
3. Initialize two pointers:
   - `i` at the start (0)
   - `j` at the end (len(s) - 1)
4. While `i < j`:
   - If both characters are vowels, swap them and move both pointers inward.  
   - If the left character is not a vowel, move `i` forward.  
   - If the right character is not a vowel, move `j` backward.  
5. Join the list back into a string and return it.  

---

## My Java Solution Approach

### Logic
We use a **two-pointer approach** with a **vowel lookup set**. One pointer starts from the beginning, and the other from the end.  
When both characters are vowels, we swap them. Otherwise, we move the corresponding pointer inward.

### Code Explanation
1. **`char[] chars = s.toCharArray();`**  
   Converts the input string into a mutable character array, as Java strings are immutable.  

2. **`HashSet<Character> vowels = new HashSet<>();`**  
   A `HashSet` is used to store all vowels for **O(1)** membership checking.  

3. **`vowelsS = "aeiouAEIOU";` and conversion to char array:**  
   We loop through all characters in `vowelsS` and add them to the `HashSet`.  

4. **`while (i < leng)` loop:**  
   Uses two pointers (`i` and `leng`) to traverse the string from both ends.  

5. **Swapping logic:**  
   - If both characters are vowels, swap them using a temporary variable.  
   - If only one is a vowel, move the non-vowel pointer toward the center.  

6. **`return new String(chars);`**  
   Converts the modified character array back to a string and returns it.  

### Methods and Libraries Used
- **`toCharArray()`** → Converts a `String` to a mutable character array.  
- **`HashSet`** → Provides constant-time lookup for vowels.  
- **`contains()`** → Checks if a character exists in the `HashSet`.  
- **`new String(chars)`** → Constructs a new string from the modified character array.  

---

## My Python Solution Approach

### Logic
The Python solution uses the same two-pointer technique as the Java version.  
We convert the string into a list (since strings in Python are immutable) and then swap vowels in place.

### Code Explanation
1. **`vow = set("aeiouAEIOU")`**  
   Creates a `set` of vowels. Sets in Python provide O(1) lookup time.  

2. **`s_list = list(s)`**  
   Converts the input string to a list to allow in-place modification.  

3. **Two pointers: `i` and `leng`**  
   - `i` starts from the beginning (0)  
   - `leng` starts from the end (`len(s) - 1`)  

4. **`while i < leng:`**  
   The loop runs until the two pointers meet.  

5. **Swapping logic:**  
   - If both `s_list[i]` and `s_list[leng]` are vowels → swap them and move both pointers inward.  
   - If `s_list[i]` is not a vowel → move `i` forward.  
   - If `s_list[leng]` is not a vowel → move `leng` backward.  

6. **`return "".join(s_list)`**  
   Joins the modified list back into a string and returns it.  

### Functions and Methods Used
- **`set()`** → Used for fast vowel membership lookup.  
- **`list(s)`** → Converts an immutable string into a mutable list.  
- **`join()`** → Efficiently concatenates list elements into a single string.  

---

## Complexities of My Approach
- **Time Complexity:** `O(n)` — each character is checked at most once.  
- **Space Complexity:** `O(n)` — for the character list and vowel set (or `O(1)` if in-place).  

---

## Self Learning
- Learned **two-pointer technique** for in-place transformations.  
- Practiced using **sets for fast membership checks**.  
- Strengthened understanding of **mutable vs immutable** data structures in Java and Python.  

---

## Can It Be Improved?
- The algorithm is already optimal at `O(n)` time.  
- Micro-optimizations:
  - Instead of manually building the vowel set in Java, use `Arrays.asList()` with a `HashSet`.  
  - For Python, predefine the vowel set as a global constant to avoid recreating it in each call.  
