# Move Zeroes

## Problem Link
[LeetCode - Move Zeroes](https://leetcode.com/problems/move-zeroes/)

## Problem Topics
Arrays, Two Pointers, In-place Modification

## Problem Description
Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.  
You must do this **in-place** without making a copy of the array.

**Constraints:**  
- Modify the array in-place with `O(1)` extra space.  
- Maintain the relative order of non-zero elements.  

## Example Input / Output

**Example 1:**  
Input: `nums = [0,1,0,3,12]`  
Output: `[1,3,12,0,0]`

**Example 2:**  
Input: `nums = [0]`  
Output: `[0]`

## Pseudocode
1. Initialize a pointer `curr = 0` to track the position for placing non-zero elements.  
2. Iterate through the array:
   - If `nums[i]` is non-zero, assign `nums[curr] = nums[i]` and increment `curr`.  
3. After the loop, fill the remaining positions from `curr` to end with zeros.  
4. Return or modify the array in-place.

## My Java Solution Approach
- **Logic:** Use two passes.  
  - First pass moves all non-zero elements to the beginning while keeping their order.  
  - Second pass fills remaining slots with zeros.

### **Code Explanation**
1. `int curr = 0;` → tracks position for the next non-zero element.  
2. First loop:  
   - If `nums[i] != 0`, assign `nums[curr] = nums[i]; curr++;`.  
   - This shifts all non-zero elements to the front in order.  
3. Second loop:  
   - Fill the remaining positions (`i = curr` to `leng - 1`) with zeros.  
4. Return `nums` (though LeetCode does not require returning since it’s in-place).

### **New Methods / Functions / Libraries Used**
- None. Pure in-place array manipulation.  
- Relies solely on two-pointer iteration.

## My Python Solution Approach
- **Logic:** Same as Java — first collect all non-zero elements at the start, then fill the rest with zeros.  

### **Code Explanation**
1. `curr = 0` → pointer for next position to fill.  
2. First loop:  
   - Iterate through `nums`, and if `nums[x] != 0`, assign `nums[curr] = nums[x]` and increment `curr`.  
3. Second loop:  
   - Fill all remaining elements from index `curr` to `leng - 1` with zeros.  
4. Return `nums` (not required for in-place modification, but included for clarity).

### **New Methods / Functions / Libraries Used**
- Simple iteration and assignment only; no library functions used.  
- `len(nums)` used to determine array length.  

## Complexities of My Approach
- **Time Complexity:** `O(n)` — each element is processed exactly once.  
- **Space Complexity:** `O(1)` — in-place modification with constant extra space.

## Self Learning
- Reinforced understanding of two-pointer pattern.  
- Practiced writing in-place array transformations.  
- Gained intuition for optimizing both time and space efficiency in array manipulation problems.

## Can It Be Improved?
- The approach is already optimal.  
- Minor improvement: Use swapping instead of overwriting to further reduce unnecessary writes (if needed for performance on large datasets).
