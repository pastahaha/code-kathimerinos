# Find Minimum and Maximum in an Array

## Problem Link
[GeeksforGeeks - Find Minimum and Maximum](https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1)

## Problem Topics
Arrays, Iteration, Brute Force

## Problem Description
Given an array of integers `arr`, find both the **minimum** and **maximum** elements in the array.  
- Return them together.  
- In Java, use the provided `Pair` class to return `(min, max)`.  
- In Python, return a list `[min, max]`.  

## Example Input / Output
**Example 1:**  
Input: `arr = [3, 5, 1, 2, 4]`  
Output: `[1, 5]`  

**Example 2:**  
Input: `arr = [10, -2, 7, 8, 0]`  
Output: `[-2, 10]`  

## Pseudocode
1. Initialize `min` as +infinity and `max` as -infinity.  
2. Iterate through the array:  
    - If current element is smaller than `min`, update `min`.  
    - If current element is larger than `max`, update `max`.  
3. Return the pair or list of `[min, max]`.  

## My Java Solution Approach
- **Logic:** Iterate once through the array, updating `min` and `max`.  
- **New Method / Class Explanation:**  
  - `Integer.MAX_VALUE` and `Integer.MIN_VALUE` are constants representing the largest and smallest possible integer values in Java.  
  - `Pair` class is used to return two values together; it provides `getKey()` and `getValue()` methods to access `min` and `max`.  
- **Step-by-step:**  
  1. Initialize `min` to `Integer.MAX_VALUE` and `max` to `Integer.MIN_VALUE`.  
  2. Loop through the array, updating `min` and `max`.  
  3. Return a new `Pair(min, max)`.  

## My Python Solution Approach
- **Logic:** Similar single-pass iteration.  
- **New Method / Function Explanation:**  
  - `float('inf')` represents positive infinity, and `float('-inf')` represents negative infinity. They are used to initialize `min` and `max` so any number in the array will replace them.  
  - Returning `[min, max]` is a standard Python list containing two elements.  
- **Step-by-step:**  
  1. Initialize `min` to `float('inf')` and `max` to `float('-inf')`.  
  2. Loop through indices of the array.  
  3. Update `min` and `max` if the current element is smaller or larger, respectively.  
  4. Return `[min, max]`.  

## Complexities of My Approach
- **Time Complexity:** `O(n)` where `n` is the size of the array (single pass).  
- **Space Complexity:** `O(1)` (constant extra space).  

## Self Learning
- Reinforced the single-pass approach to find min and max efficiently.  
- Practiced using language-specific constructs (`Pair` in Java, `float('inf')` in Python).  

## Can It Be Improved?
- Yes, using **pairwise comparison**, we can reduce the number of comparisons slightly (especially for large arrays).  
- For very large datasets, this method is already efficient in terms of both time and space.
