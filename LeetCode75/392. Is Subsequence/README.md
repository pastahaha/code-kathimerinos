# Is Subsequence

## Problem Link
[LeetCode - Is Subsequence](https://leetcode.com/problems/is-subsequence/)

## Problem Topics
Two Pointers, String Matching, Greedy, Linear Scan

## Problem Description
Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` otherwise.  

A subsequence of a string is a new string that is formed from the original string by deleting some (or none) of the characters without disturbing the relative positions of the remaining characters.

**Constraints:**  
- Both strings consist only of lowercase English letters.  
- The time complexity should be linear (`O(n)`), where `n` is the length of `t`.  

## Example Input / Output

**Example 1:**  
Input: `s = "abc"`, `t = "ahbgdc"`  
Output: `true`  
Explanation: `'a'`, `'b'`, and `'c'` appear in order in `t`.

**Example 2:**  
Input: `s = "axc"`, `t = "ahbgdc"`  
Output: `false`  
Explanation: `'x'` does not appear after `'a'` in `t`.

## Pseudocode
1. If `s` is empty, return `true`.  
2. Initialize two pointers:
   - `i` → index for `t`
   - `j` → index for `s`
3. Iterate through `t`:
   - If `t[i] == s[j]`, move both pointers forward.  
   - Else, move only `i` forward.  
4. After the loop, if `j == len(s)`, return `true`; otherwise, return `false`.

## My Java Solution Approach
- **Logic:** Use two pointers — one for each string.  
  - Traverse `t`, advancing the pointer in `s` only when matching characters are found.  
  - If all characters in `s` are matched, `s` is a subsequence of `t`.

### **Code Explanation**
1. `if (s==null || s.isEmpty()) return true;` → handles empty subsequence case.  
2. `int i = 0; int curr = 0;` → two pointers for `t` and `s`.  
3. While traversing `t`, if characters match, increment `curr`.  
4. After traversal, check if `curr == s.length()`. If yes, all characters of `s` matched.  

### **New Methods / Functions / Libraries Used**
- `String.charAt(index)` → retrieves character at specified position.  
- Simple pointer manipulation and conditional checks.

## My Python Solution Approach
- **Logic:** Same as Java — iterate through `t` and move a pointer through `s` when a match is found.  

### **Code Explanation**
1. `if not s: return True` → handles empty string edge case.  
2. Initialize two pointers:  
   - `i` → for `t`  
   - `it` → for `s`  
3. Traverse through `t`:
   - If characters match, move `it` forward.  
   - Always move `i` forward.  
4. If `it == len(s)` after traversal, return `True`, else `False`.  

### **New Methods / Functions / Libraries Used**
- Basic iteration and conditional statements; no external libraries used.  
- `len()` → retrieves length of the string.

## Complexities of My Approach
- **Time Complexity:** `O(n)` — where `n` is the length of `t`.  
- **Space Complexity:** `O(1)` — uses constant extra space.  

## Self Learning
- Strengthened understanding of two-pointer traversal logic in string matching.  
- Practiced efficient subsequence verification without extra data structures.  
- Reinforced linear-time string comparison techniques.

## Can It Be Improved?
- Already optimal for a single subsequence check.  
- For multiple subsequence checks against a fixed `t`, we can preprocess `t` using binary search over character indices for faster lookups — but that’s a different problem variant (“Follow-up” in LeetCode).
