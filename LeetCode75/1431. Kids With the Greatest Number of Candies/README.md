# Kids With the Greatest Number of Candies

## Problem Link
[LeetCode - Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)

## Problem Topics
Arrays, Simulation, Iteration, Brute Force

## Problem Description
Given an array `candies` where `candies[i]` represents the number of candies the `i`-th kid has, and an integer `extraCandies`, return a **boolean list** indicating for each kid whether they can have the greatest number of candies among all kids if they receive all `extraCandies`.  

- A kid is considered to have the greatest number of candies if no other kid has more candies than them after receiving extra candies.  

## Example Input / Output
**Example 1:**  
Input: `candies = [2,3,5,1,3]`, `extraCandies = 3`  
Output: `[True, True, True, False, True]`  

**Example 2:**  
Input: `candies = [4,2,1,1,2]`, `extraCandies = 1`  
Output: `[True, False, False, False, False]`  

## Pseudocode
1. Initialize an empty result list.  
2. For each kid, calculate `current_candies = candies[i] + extraCandies`.  
3. Check if `current_candies` is greater than or equal to all other kids’ candies.  
4. Append `True` or `False` to the result list accordingly.  
5. Return the result list.  

## My Java Solution Approach
- **Logic:** Iterate through the `candies` array, adding `extraCandies` to each kid’s count, then check if it is the maximum among all kids.  
- **Code Explanation:**  
  1. `List<Boolean> result = new ArrayList<>();` → initializes a list to store boolean results.  
  2. Loop through each kid using `for(int x=0; x< candies.length; x++)`.  
  3. `int curr = candies[x] + extraCandies;` → calculates the candies this kid would have after getting extra candies.  
  4. `result.add(checkMax(curr, candies));` → checks if `curr` is the maximum and appends the result.  
  5. `private Boolean checkMax(int curr, int[] candies)` → helper method: loops through all kids’ candies and returns `false` if any kid has more than `curr`; otherwise returns `true`.  
  6. Finally, return `result`.  

- **New Methods / Functions / Libraries Explanation:**  
  - `ArrayList<Boolean>`: dynamically sized list to store boolean values.  
  - `add()`: adds an element to the list.  
  - Helper method `checkMax()`: used to encapsulate the comparison logic.  

## My Python Solution Approach
- **Logic:** Same as Java: for each kid, add `extraCandies` and check if it is the largest.  
- **Code Explanation:**  
  1. `op = []` → initializes the result list.  
  2. `while i != len(candies):` → loop through each kid.  
  3. `curr = candies[i] + extraCandies` → calculates candies after giving extra.  
  4. `op.append(self.checkMax(curr, candies))` → appends `True` or `False` depending on whether `curr` is the largest.  
  5. `def checkMax(self, curr, candies)` → helper method: loops through all elements in `candies`; if any element is greater than `curr`, return `False`; otherwise return `True`.  
  6. Return `op` as the final result.  

- **New Methods / Functions / Libraries Explanation:**  
  - `list.append()`: adds an element to the end of a list.  
  - Helper method `checkMax()`: modularizes the maximum check.  

## Complexities of My Approach
- **Time Complexity:** `O(n^2)` — for each kid, we check against all others (`n` kids).  
- **Space Complexity:** `O(n)` — for the output list storing boolean values.  

## Self Learning
- Practiced modularizing code using helper functions in both Java and Python.  
- Learned clear separation of logic and utility functions for readability.  

## Can It Be Improved?
- Yes, by **precomputing the maximum candy count** among all kids first, we can reduce the time complexity to `O(n)` instead of `O(n^2)`:
  - Compute `max_candies = max(candies)`.  
  - For each kid, check if `candies[i] + extraCandies >= max_candies`.  
  - Append the boolean result to the list.  
- This avoids repeatedly comparing with all elements.
