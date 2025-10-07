# Linear Search

## Problem Link
[GeeksforGeeks - Linear Search](https://practice.geeksforgeeks.org/problems/linear-search/1)

## Problem Topics
Arrays, Searching, Brute Force

## Problem Description
Given an array `arr` and a target element `x`, return the **index** of `x` in the array if it exists; otherwise, return `-1`.  
- The array may not be sorted.  
- If `x` appears multiple times, return the index of the **first occurrence**.  

## Example Input / Output
**Example 1:**  
Input: `arr = [1, 3, 5, 7, 9]`, `x = 5`  
Output: `2`  

**Example 2:**  
Input: `arr = [2, 4, 6, 8]`, `x = 10`  
Output: `-1`  

## Pseudocode
1. Loop through each element in the array.  
2. If the current element equals `x`, return its index.  
3. If the loop ends without finding `x`, return `-1`.  

## My Java Solution Approach
- Use a simple `for` loop to iterate through the array.  
- Compare each element with the target `x`.  
- Return the index immediately if found.  
- Return `-1` if the loop finishes without a match.  

## My Python Solution Approach
- Use a `for` loop over the index range of the array.  
- Compare each element with the target `x`.  
- Return the index immediately if found.  
- Return `-1` if the element is not in the array.  

## Complexities of My Approach
- **Time Complexity:** `O(n)` where `n` is the length of the array.  
- **Space Complexity:** `O(1)` since no extra space is used.  

## Self Learning
- Practiced iterating arrays in both Java and Python.  
- Reinforced the concept of linear search as a basic but essential algorithm.  

## Can It Be Improved?
- If the array is sorted, a **binary search** could reduce time complexity to `O(log n)`.  
- In Python, using `arr.index(x)` is a built-in alternative for simplicity.  
- For large datasets, using a **hash map** can achieve `O(1)` average lookup if multiple searches are required.
