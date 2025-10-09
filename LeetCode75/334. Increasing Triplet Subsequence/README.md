# Increasing Triplet Subsequence

## Problem Link
[LeetCode - Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/)

## Problem Topics
Arrays, Greedy, Dynamic Programming, Sequence Tracking, In-place Computation

## Problem Description
Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`.  
Otherwise, return `false`.

**Constraints:**  
- Must solve in `O(n)` time and `O(1)` space.  
- No need to return the actual triplet, only whether it exists.

## Example Input / Output

**Example 1:**  
Input: `nums = [1,2,3,4,5]`  
Output: `true`  
Explanation: The increasing triplet `[1,2,3]` exists.

**Example 2:**  
Input: `nums = [5,4,3,2,1]`  
Output: `false`  
Explanation: No increasing triplet exists.

**Example 3:**  
Input: `nums = [2,1,5,0,4,6]`  
Output: `true`  
Explanation: The increasing triplet `[1,4,6]` exists.

## Pseudocode
1. Initialize two variables `first` and `second` to infinity.  
2. Iterate over the array:
   - If current number ≤ `first`, update `first`.  
   - Else if current number ≤ `second`, update `second`.  
   - Else, a number larger than both exists → return `true`.  
3. If iteration completes without returning, return `false`.

## My Java Solution Approach
- **Logic:** Keep track of the smallest and second smallest numbers seen so far (`first` and `second`).  
- When a number bigger than both is found, we have an increasing triplet.

### **Code Explanation**
1. `float first = Float.POSITIVE_INFINITY, second = Float.POSITIVE_INFINITY;` → initialize placeholders for smallest and second smallest numbers.  
2. Iterate through `nums`:
   - `if(nums[i] <= first) first = nums[i];` → update smallest number.  
   - `else if(nums[i] <= second) second = nums[i];` → update second smallest number.  
   - `else return true;` → current number is bigger than both → triplet found.  
3. Return `false` if no triplet is found.

### **New Methods / Functions / Libraries Used**
- `Float.POSITIVE_INFINITY` → used to initialize variables to a very large value.  
- Simple comparisons, no additional libraries needed.  

## My Python Solution Approach
- **Logic:** Same as Java — track the smallest and second smallest numbers while iterating.  

### **Code Explanation**
1. `one = float('inf'); two = float('inf')` → initialize placeholders.  
2. For each number `n` in `nums`:
   - `if n <= one: one = n` → update smallest number.  
   - `elif n <= two: two = n` → update second smallest number.  
   - `else: return True` → found a number bigger than both → triplet exists.  
3. Return `False` if no triplet found.

### **New Methods / Functions / Libraries Used**
- `float('inf')` → represents infinity.  
- Simple comparison and assignment logic.

## Complexities of My Approach
- **Time Complexity:** `O(n)` — iterate over array once.  
- **Space Complexity:** `O(1)` — only two extra variables used.

## Self Learning
- Reinforced the greedy approach for subsequence problems.  
- Learned to track multiple thresholds (`first` and `second`) efficiently.  
- Practiced O(1) space solutions for sequence detection problems.

## Can It Be Improved?
- This is already optimal (`O(n)` time, `O(1)` space).  
- Alternative solutions involve dynamic programming with `O(n^2)` time or binary search, but less efficient for large arrays.
