# Greatest Common Divisor of Strings

## Problem Link
[LeetCode - GCD of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

## Problem Topics
Strings, Mathematics, GCD, Brute Force, String Manipulation

## Problem Description
Given two strings `str1` and `str2`, return the **largest string `X`** such that:  
- `X` can be concatenated some number of times to get `str1`.  
- `X` can be concatenated some number of times to get `str2`.  

If no such string exists, return an empty string `""`.  

**Key Observation:**  
- For strings `str1` and `str2`, a common divisor exists if `str1 + str2 == str2 + str1`.  
- The length of the GCD string is the **GCD of the lengths** of `str1` and `str2`.  

## Example Input / Output
**Example 1:**  
Input: `str1 = "ABCABC"`, `str2 = "ABC"`  
Output: `"ABC"`  

**Example 2:**  
Input: `str1 = "ABABAB"`, `str2 = "ABAB"`  
Output: `"AB"`  

**Example 3:**  
Input: `str1 = "LEET"`, `str2 = "CODE"`  
Output: `""`  

## Pseudocode
1. If either string is empty, return `""`.  
2. Check if `str1 + str2 == str2 + str1`. If not, return `""`.  
3. Compute `gcd(len(str1), len(str2))` → call it `k`.  
4. Return the substring of `str1` from index `0` to `k`.  

## My Java Solution Approach
- **Logic:**  
  1. Check if strings can form a common repeated pattern by comparing concatenations.  
  2. Compute GCD of string lengths using a helper method.  
  3. Return substring of `str1` up to GCD length.  
- **New Methods / Functions / Classes Explanation:**  
  - `str1.substring(0, x)`: returns a substring from index `0` to `x-1`.  
  - `str1.length()`: returns the number of characters in the string.  
  - `equals()`: compares two strings for exact equality.  
  - `gcd(int a, int b)`: uses Euclidean algorithm to find greatest common divisor.  
- **Step-by-step:**  
  1. Handle null or empty strings → return `""`.  
  2. Check concatenation condition: `(str1 + str2).equals(str2 + str1)`.  
  3. Compute `gcd(str1.length(), str2.length())`.  
  4. Return `str1.substring(0, gcd)` as the GCD string.  

## My Python Solution Approach
- **Logic:** Same approach using Python syntax.  
- **New Methods / Functions / Libraries Explanation:**  
  - `str1 + str2`: concatenates two strings.  
  - `len(str1)`: gets length of the string.  
  - Slicing `str1[:num1]`: returns substring from index `0` to `num1-1`.  
  - `%` operator: used in Euclidean algorithm for GCD.  
- **Step-by-step:**  
  1. Handle empty strings → return `""`.  
  2. Check if `str1 + str2 != str2 + str1` → return `""`.  
  3. Use while loop to compute `gcd(len(str1), len(str2))`.  
  4. Return `str1[:gcd_length]` as the result.  

## Complexities of My Approach
- **Time Complexity:** `O(n + m)` where `n` and `m` are lengths of `str1` and `str2` (for concatenation check).  
- **Space Complexity:** `O(1)` additional space, aside from the substring returned.  

## Self Learning
- Learned how **GCD of lengths** relates to repeated string patterns.  
- Practiced Euclidean algorithm in both Java and Python.  
- Learned a concise trick for checking repeated string compatibility: `str1 + str2 == str2 + str1`.  

## Can It Be Improved?
- Already optimal for both time and space.  
- Minor improvement: avoid creating full concatenation strings in very large inputs by checking substring patterns iteratively.
