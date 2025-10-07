# Merge Strings Alternately

## Problem Link
[LeetCode - Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)

## Problem Topics
Strings, Two Pointers, Simulation

## Problem Description
Given two strings `word1` and `word2`, merge them **alternately** character by character.  
- Start with the first character of `word1`, then the first character of `word2`, then the second character of `word1`, and so on.  
- If one string is longer, append the remaining characters at the end of the merged string.  

## Example Input / Output
**Example 1:**  
Input: `word1 = "abc"`, `word2 = "pqr"`  
Output: `"apbqcr"`  

**Example 2:**  
Input: `word1 = "ab"`, `word2 = "pqrs"`  
Output: `"apbqrs"`  

**Example 3:**  
Input: `word1 = "abcd"`, `word2 = "pq"`  
Output: `"apbqcd"`  

## Pseudocode
1. Initialize two pointers `i` and `j` to `0`.  
2. Initialize an empty result container (`StringBuilder` in Java, list in Python).  
3. While both pointers are within their respective string lengths:  
    - Append the character from `word1[i]` and `word2[j]` to the result.  
    - Increment both `i` and `j`.  
4. Append any remaining characters from `word1` or `word2`.  
5. Return the result as a string.  

## My Java Solution Approach
- Use a `StringBuilder` to efficiently construct the merged string.  
- Maintain two pointers `i` and `j` for `word1` and `word2`.  
- Append characters alternately from both strings until one ends.  
- Append the remaining substring from the longer string using `substring()`.  
- Return the final merged string.  

## My Python Solution Approach
- Use a list `res` to build the merged string, which is efficient for multiple appends.  
- Maintain two pointers `i` and `j`.  
- Append characters alternately from both strings.  
- Use slicing to append any leftover characters from the longer string.  
- Join the list into a single string before returning.  

## Complexities of My Approach
- **Time Complexity:** `O(n + m)` where `n` and `m` are the lengths of `word1` and `word2`.  
- **Space Complexity:** `O(n + m)` for storing the merged string.  

## Self Learning
- Learned the importance of handling edge cases where strings are of unequal lengths.  
- Efficient string concatenation differs between languages: `StringBuilder` in Java vs list + join in Python.  

## Can It Be Improved?
- Minor optimization: Avoid calculating lengths multiple times by storing them in variables.  
- Could use `zip_longest` in Python for a more Pythonic approach.  
- Overall, the approach is already optimal in terms of time and space for this problem.
