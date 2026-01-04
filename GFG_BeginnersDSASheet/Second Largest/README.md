```markdown
# Second Largest

**Problem Link:** [GeeksforGeeks - Second Largest](https://www.geeksforgeeks.org/problems/second-largest3735/1)

**Problem Topics:** Arrays, Sorting, Searching

**Problem Description:** Given an array of positive integers `arr[]`, return the second largest element from the array. If the second largest element doesn't exist then return -1.

**Problem Example Output:**
- **Input:** `arr = [12, 35, 1, 10, 34, 1]`
- **Output:** `34`

---

### Pseudocode
1. Initialize two variables `lar` and `s_lar` to -1.
2. Iterate through each element `num` in the array:
    - If `num` is greater than `lar`:
        - Update `s_lar` to the current `lar`.
        - Update `lar` to `num`.
    - Else if `num` is smaller than `lar` but greater than `s_lar`:
        - Update `s_lar` to `num`.
3. Return `s_lar`.

---

### My Java Solution Approach
- **Strategy:** I used a **single-pass approach** with two pointers/variables. By maintaining the largest and second-largest values simultaneously, I ensure that every element is checked only once. The condition `arr[i] < lar` ensures that we don't count the largest element twice if it appears multiple times.
- **Methods/Functions Used:**
    - `arr.length`: Used to iterate through the array using a standard `for` loop.
    - Basic comparison operators (`>`, `<`) to rank the elements.

### My Python Solution Approach
- **Strategy:** The logic mirrors the Java solution, utilizing Python's efficient membership iteration (`for num in arr`). This makes the code cleaner by directly accessing the values instead of their indices.
- **Methods/Functions Used:**
    - `for num in arr`: This is a "for-each" loop in Python, which is more idiomatic and often faster than indexing via `range(len(arr))`.
    - `elif`: Used for conditional branching to check for the second largest only if the current number isn't the new largest.

---

### Complexities of My Approach
- **Time Complexity:** $O(n)$ — We traverse the array exactly once.
- **Space Complexity:** $O(1)$ — We only use two integer variables (`lar` and `s_lar`) regardless of input size.

---

### Self Learning
**Can it be improved?**
The current $O(n)$ time and $O(1)$ space complexity is already the most efficient way to solve this problem.

**How?**
- **Alternative (Sorting):** One could sort the array in descending order and pick the second distinct element. However, that would take $O(n \log n)$ time, which is slower than this linear approach.
- **Edge Cases:** The current code handles cases where all elements are the same or only one element exists by initializing variables to -1, which is the required return value for "not found."

```