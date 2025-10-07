# Find Maximum in a Bitonic Array

## Problem Link
[GeeksforGeeks - Maximum in Bitonic Array](https://practice.geeksforgeeks.org/problems/maximum-of-bitonic-array/1)

## Problem Topics
Arrays, Binary Search, Divide & Conquer, Bit Manipulation

## Problem Description
Given a **bitonic array** (an array which is first strictly increasing then strictly decreasing), find the **maximum element** in the array.  
- The array has no duplicate elements.  
- A bitonic array of length `n` satisfies: `arr[0] < arr[1] < ... < arr[k] > arr[k+1] > ... > arr[n-1]` for some `k`.  

## Example Input / Output
**Example 1:**  
Input: `arr = [1, 3, 8, 12, 4, 2]`  
Output: `12`  

**Example 2:**  
Input: `arr = [3, 8, 3, 1]`  
Output: `8`  

## Pseudocode
1. Initialize `start = 0` and `end = n-1`.  
2. While `start <= end`:  
   - Compute `mid = (start + end) / 2`.  
   - If `arr[mid] > arr[mid-1]` and `arr[mid] > arr[mid+1]`, return `arr[mid]`.  
   - If `arr[mid] > arr[mid-1]` and `arr[mid] < arr[mid+1]`, move right (`start = mid + 1`).  
   - Else move left (`end = mid - 1`).  
3. Handle edge cases for `mid = 0` or `mid = n-1`.  
4. Return the maximum found.  

## My Java Solution Approach
- **Logic:** Use **binary search** to find the peak in a bitonic array.  
- **New Methods / Functions / Classes Explanation:**  
  - `(start + end) / 2` calculates the middle index.  
  - Ternary operator `(condition) ? value1 : value2` is used to select the maximum in edge cases.  
  - No extra space is required.  
- **Step-by-step:**  
  1. Initialize `start = 0` and `end = arr.length - 1`.  
  2. While `start <= end`, calculate `mid`.  
  3. Check if `arr[mid]` is greater than neighbors → return it if true.  
  4. Decide the direction based on slope: increasing → move right, decreasing → move left.  
  5. Handle edges (`mid = 0` or `mid = n-1`).  

## My Python Solution Approach
- **Logic:** Same binary search approach.  
- **New Methods / Functions / Libraries Explanation:**  
  - `//` operator performs **integer division** in Python.  
  - `max(arr[-1], arr[-2])` selects the larger of the last two elements.  
- **Step-by-step:**  
  1. Initialize `start = 0` and `end = len(arr) - 1`.  
  2. While `start <= end`, calculate `mid`.  
  3. If `arr[mid]` is greater than neighbors, return it.  
  4. If slope is increasing, move `start = mid + 1`, else `end = mid - 1`.  
  5. Handle edge cases at the start or end of the array.  

## Complexities of My Approach
- **Time Complexity:** `O(log n)` — binary search approach.  
- **Space Complexity:** `O(1)` — no extra space used.  

## Self Learning
- Learned to apply **binary search on non-trivial arrays** (bitonic arrays).  
- Reinforced handling edge cases carefully (`mid = 0` or `mid = n-1`).  

## Can It Be Improved?
- Already optimal in time (`O(log n)`) and space (`O(1)`).  
- Could simplify Python code slightly using `max(arr[mid], arr[mid+1], arr[mid-1])` in boundary-safe checks, but binary search approach is preferred for efficiency.
