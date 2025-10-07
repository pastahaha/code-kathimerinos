# Find Missing Number in Array (XOR Method)

## Problem Link
[GeeksforGeeks - Find the Missing Number](https://practice.geeksforgeeks.org/problems/missing-number-in-array-1587115620/1)

## Problem Topics
Arrays, Bit Manipulation, XOR, Mathematics

## Problem Description
Given an array `arr` containing `n-1` distinct integers from `1` to `n`, find the **missing number**.  
- The array contains integers in the range `1` to `n` inclusive.  
- Exactly one number is missing.  
- Use the XOR operation to find it efficiently without extra space.  

## Example Input / Output
**Example 1:**  
Input: `arr = [1, 2, 4, 5]`  
Output: `3`  

**Example 2:**  
Input: `arr = [2, 3, 1, 5]`  
Output: `4`  

## Pseudocode
1. Initialize `xor_all = 0` and `xor_arr = 0`.  
2. XOR all numbers from `1` to `n` → store in `xor_all`.  
3. XOR all elements in the array → store in `xor_arr`.  
4. Return `xor_all XOR xor_arr` → gives the missing number.  

## My Java Solution Approach
- **Logic:** Use XOR property: `a ^ a = 0` and `a ^ 0 = a`. XORing all numbers from `1` to `n` and the array elements cancels out all present numbers, leaving the missing number.  
- **New Methods / Functions / Classes Explanation:**  
  - `^` operator in Java performs **bitwise XOR**.  
  - `arr.length` gives the size of the array.  
- **Step-by-step:**  
  1. Compute XOR of all numbers from `1` to `n` using a loop → `all`.  
  2. Compute XOR of all elements in the array → `arrSum`.  
  3. Return `all ^ arrSum`.  

## My Python Solution Approach
- **Logic:** Same XOR-based approach as in Java.  
- **New Methods / Functions / Libraries Explanation:**  
  - `^` operator in Python performs **bitwise XOR**.  
  - `len(arr)` returns the number of elements in the array.  
- **Step-by-step:**  
  1. Compute XOR of all numbers from `1` to `n` → `temp`.  
  2. Compute XOR of all array elements → `arrSum`.  
  3. Return `temp ^ arrSum`.  

## Complexities of My Approach
- **Time Complexity:** `O(n)` — single pass through numbers and array.  
- **Space Complexity:** `O(1)` — no extra space used except variables.  

## Self Learning
- Learned a clever use of **XOR** to find a missing number efficiently.  
- Bit manipulation can solve problems without extra memory and without summing integers.  

## Can It Be Improved?
- Already optimal in time and space.  
- Alternative methods:  
  - Sum formula: `n*(n+1)/2 - sum(arr)` (careful with integer overflow in some languages).  
  - Using a boolean or hash array (uses extra space).  
