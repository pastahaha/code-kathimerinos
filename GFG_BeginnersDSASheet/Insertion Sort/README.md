# Insertion Sort

**Problem Link:** [GeeksforGeeks - Insertion Sort](https://www.geeksforgeeks.org/problems/insertion-sort/1)

**Problem Topics:** Sorting, Arrays

**Problem Description:** The task is to complete the `insertionSort()` function which is used to implement Insertion Sort. The array should be sorted in-place in ascending order.

**Problem Example Output:**
- **Input:** `arr = [4, 1, 3, 9, 7]`
- **Output:** `[1, 3, 4, 7, 9]`

---

### Pseudocode
1. Iterate from the second element (index 1) to the end of the array.
2. Store the current element in a variable `temp`.
3. Compare `temp` with the elements before it (to its left).
4. Shift the elements of the sorted segment (elements to the left) one position to the right if they are greater than `temp`.
5. Insert `temp` into its correct sorted position.

---

### My Java Solution Approach
- **Strategy:** I implemented the classic **Insertion Sort** algorithm. It works similarly to how we sort playing cards in our hands. I treat the first element as already sorted and then "insert" the subsequent elements into their correct relative positions by shifting larger elements to the right.
- **Methods/Functions Used:**
    - `arr.length`: Used to control the outer loop.
    - `while` loop: Used to perform the "shifting" operation as long as the elements to the left are greater than the `temp` value and we haven't hit the start of the array.

### My Python Solution Approach
- **Strategy:** Identical logic to the Java implementation. I used a `range` starting from 1 since a single-element array (the first element) is technically already sorted.
- **Methods/Functions Used:**
    - `range(1, len(arr))`: Generates indices starting from 1.
    - `len(arr)`: Gets the size of the list.
    - `j -= 1`: Python's decrement syntax used within the `while` loop to move backward through the sorted portion of the list.

---

### Complexities of My Approach
- **Time Complexity:** - **Worst/Average Case:** $O(n^2)$ — Occurs when the array is sorted in reverse order.
    - **Best Case:** $O(n)$ — Occurs when the array is already sorted (the `while` loop never executes).
- **Space Complexity:** $O(1)$ — The sorting is done in-place without using extra auxiliary space.

---

### Self Learning
**Can it be improved?**
For general-purpose sorting of large datasets, yes. 

**How?**
- **Algorithm Choice:** For much larger arrays, algorithms like **QuickSort**, **MergeSort**, or **HeapSort** are preferred as they offer $O(n \log n)$ time complexity.
- **Binary Insertion Sort:** You could use **Binary Search** to find the correct position for `temp` instead of linear scanning. This reduces comparisons, but the overall time remains $O(n^2)$ due to shifting.