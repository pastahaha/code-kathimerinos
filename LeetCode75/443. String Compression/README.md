# String Compression

## Problem Link
[LeetCode - String Compression](https://leetcode.com/problems/string-compression/)

## Problem Topics
Strings, Two Pointers, In-place Modification, Array Manipulation

## Problem Description
Given an array of characters `chars`, compress it **in-place**.  
The compressed length should be minimized, and after compression, return the new length of the array.  

**Rules:**  
- For each group of consecutive repeating characters, write the character followed by the count (if count > 1).  
- Do not allocate extra space for another array — modify `chars` in-place with `O(1)` extra memory.  

## Example Input / Output

**Example 1:**  
Input: `chars = ["a","a","b","b","c","c","c"]`  
Output: `6`  
Explanation: `chars` becomes `["a","2","b","2","c","3"]`.

**Example 2:**  
Input: `chars = ["a"]`  
Output: `1`  
Explanation: `chars` stays `["a"]`.

**Example 3:**  
Input: `chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]`  
Output: `4`  
Explanation: `chars` becomes `["a","b","1","2"]`.

## Pseudocode
1. Initialize two pointers `left` and `right` at 0.  
2. Iterate through the array using `right`:
   - Track current character `char` and a `count` of consecutive occurrences.  
   - Increment `right` while the character matches and count them.  
3. Write the character to `chars[left]` and increment `left`.  
4. If `count > 1`, write each digit of the count to `chars` starting from `left`.  
5. Continue until all characters are processed.  
6. Return `left` as the new length of the compressed array.

## My Java Solution Approach
- **Logic:** Use two pointers `left` and `right` to identify groups of repeating characters, write the compressed form in-place.  

### **Code Explanation**
1. `int left=0, right=0;` → initialize pointers for reading and writing.  
2. Loop through `chars` with `right` to count consecutive identical characters.  
3. Assign `chars[left] = curr` → write the character and increment `left`.  
4. If `count > 1`, convert count to string and write each digit in order to `chars` starting from `left`.  
5. Return `left` as the length of compressed array.

### **New Methods / Functions / Libraries Used**
- `String.valueOf(count)` → converts integer count to string.  
- `countString.charAt(i)` → iterates over digits of count.  
- Standard array operations and two-pointer logic.

## My Python Solution Approach
- **Logic:** Same as Java — two pointers to detect sequences, write character and count digits in-place.  

### **Code Explanation**
1. `left=0, right=0` → initialize pointers.  
2. Loop through `chars` with `right`, track `count` of consecutive occurrences.  
3. Write `chars[left] = char` and increment `left`.  
4. If `count > 1`, convert `count` to string and write each digit to `chars[left]`.  
5. Return `left` as new compressed length.

### **New Methods / Functions / Libraries Used**
- `str(count)` → converts integer to string in Python.  
- Simple iteration and assignment for in-place modification.

## Complexities of My Approach
- **Time Complexity:** `O(n)` — each character is processed once.  
- **Space Complexity:** `O(1)` — only a few variables are used, in-place modification.  

## Self Learning
- Practiced in-place array modification with two pointers.  
- Learned careful handling of consecutive groups and count digit writing.  
- Reinforced understanding of space optimization in array problems.

## Can It Be Improved?
- Already optimal in `O(n)` time and `O(1)` space.  
- Minor readability improvement: encapsulate count writing in a helper function for cleaner code.
