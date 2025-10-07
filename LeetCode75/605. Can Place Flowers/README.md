# Can Place Flowers

## Problem Link
[LeetCode - Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)

## Problem Topics
Arrays, Greedy, Simulation

## Problem Description
You have a long flowerbed where some plots are planted and some are empty. Plots are represented as an integer array containing 0 (empty) and 1 (not empty).  

You want to plant `n` new flowers in the flowerbed **without violating the rule** that no two flowers can be planted in adjacent plots.  

Return `true` if `n` new flowers can be planted in the flowerbed without violating the rule, otherwise `false`.

## Example Input / Output
**Example 1:**  
Input: `flowerbed = [1,0,0,0,1]`, `n = 1`  
Output: `true`  

**Example 2:**  
Input: `flowerbed = [1,0,0,0,1]`, `n = 2`  
Output: `false`  

## Pseudocode
1. If `n` is 0 → return `True` (nothing to plant).  
2. Iterate through each index `i` in `flowerbed`.  
3. If the current plot `i` is empty (`0`):  
   - Check if both neighbors (`i-1` and `i+1`) are either empty or out of bounds.  
   - If both are valid, plant a flower (`flowerbed[i] = 1`) and reduce `n` by 1.  
   - If all flowers are planted (`n == 0`), return `True`.  
4. After the loop, if not all flowers are planted, return `False`.  

---

## My Java Solution Approach

### Logic
We loop through the flowerbed array and try to plant flowers greedily wherever possible without breaking the adjacency rule.

### Code Explanation
1. **`if (n == 0) return true;`**  
   - Base case: if no flowers need to be planted, the condition is automatically satisfied.  
2. **`for (int i = 0; i < leng; i++)`**  
   - Iterates through each plot in the flowerbed.  
3. **`if (flowerbed[i] == 0)`**  
   - Only consider empty plots for planting.  
4. **Neighbor Checks:**  
   - `(i == 0 || flowerbed[i - 1] == 0)` ensures the left neighbor is empty or doesn’t exist.  
   - `(i == leng - 1 || flowerbed[i + 1] == 0)` ensures the right neighbor is empty or doesn’t exist.  
5. **If both neighbors are valid:**  
   - Plant a flower: `flowerbed[i] = 1`.  
   - Decrement `n` → `n -= 1`.  
   - If all flowers are planted (`n == 0`), return `true`.  
6. **If the loop ends without satisfying `n == 0`**, return `false`.  

### Methods and Libraries Used
- **`flowerbed[i]` indexing:** direct access to array elements.  
- **Logical short-circuiting (`||`):** helps handle edge conditions (first and last plot) cleanly.  

---

## My Python Solution Approach

### Logic
The logic mirrors the Java approach. We loop through the `flowerbed` list and plant flowers whenever possible, respecting adjacency constraints.

### Code Explanation
1. **`if n == 0: return True`**  
   - Base condition: if no flowers to plant, return immediately.  
2. **Loop through the indices using `for i in range(leng):`**  
   - Iterate over each plot in the flowerbed.  
3. **Condition to check before planting:**  
   - `flowerbed[i] == 0` → the current plot must be empty.  
   - `(i == 0 or flowerbed[i-1] == 0)` → left neighbor check.  
   - `(i == leng-1 or flowerbed[i+1] == 0)` → right neighbor check.  
4. **If all conditions pass:**  
   - Set `flowerbed[i] = 1` (plant the flower).  
   - Decrease `n` by 1.  
   - If `n == 0`, return `True`.  
5. **If loop finishes and flowers remain:**  
   - Return `False`.  

### Methods and Functions Used
- **List indexing:** `flowerbed[i]` used for direct element access and modification.  
- **Short-circuit evaluation (`or`):** avoids out-of-range errors for boundary conditions.  

---

## Complexities of My Approach
- **Time Complexity:** `O(n)` — we traverse the array once.  
- **Space Complexity:** `O(1)` — in-place modification of the input array, no extra storage used.  

---

## Self Learning
- Learned how to handle **boundary edge cases** using short-circuit conditions.  
- Practiced writing **greedy algorithms** in both Python and Java.  
- Reinforced the concept of **in-place array modification** to optimize space.  

---

## Can It Be Improved?
- Current solution is already optimal with `O(n)` time and `O(1)` space.  
- Minor optimization:  
  - We can skip one index after planting a flower since adjacent plots can’t be used (`i += 2` instead of `i++`).  
  - This avoids unnecessary checks and improves runtime slightly.
