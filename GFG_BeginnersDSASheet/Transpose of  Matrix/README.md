# Transpose Matrix

## Problem Link
[Transpose Matrix - GeeksforGeeks](https://www.geeksforgeeks.org/problems/transpose-of-matrix-1587115621/1)

## Problem Topics
- Matrix  
- Data Structures  
- Array  

## Problem Description
Given a square matrix `mat` of size `n x n`, find the transpose of the matrix.  
The transpose of a matrix is obtained by switching its rows and columns.

## Problem Example Output

**Input:**
```text
mat = [[1, 1, 1],
       [2, 2, 2],
       [3, 3, 3]]
```

**Output:**

```text
[[1, 2, 3],
 [1, 2, 3],
 [1, 2, 3]]
```

## Pseudocode

1. Iterate through each row `i` from `0` to `n-1`.
2. For each row, iterate through each column `j` starting from `i + 1` to `n-1`.
3. Swap the elements at `mat[i][j]` and `mat[j][i]`.
4. (Optional) Convert the result to the required data structure format.

## My Java Solution Approach

* I implemented an **in-place transpose** logic first to optimize space on the original array.
* **New Methods / Classes Used:**

  * `ArrayList<ArrayList<Integer>>`: Used to store the final result as per the problem's return type.
  * `ArrayList.add()`: Used to dynamically build the nested list structure.
* **How it works:**
  I used a nested loop where the inner loop starts at `i + 1`. This ensures we only swap elements across the diagonal once. After performing the in-place swap on the primitive `int[][]` array, I manually converted it into an `ArrayList` structure to satisfy the method signature.

## My Python Solution Approach

* I performed an **in-place swap** using Python's unique syntax.
* **New Methods / Features Used:**

  * `mat[i][j], mat[j][i] = mat[j][i], mat[i][j]`: Pythonic way to swap two variables without a temporary variable.
* **How it works:**
  By iterating through the upper triangle of the matrix (where `j > i`), each element `(i, j)` is swapped with its corresponding element `(j, i)` across the main diagonal.

## Complexities of My Approach

* **Time Complexity:**

  * `O(n^2)` — We visit roughly half of the elements in the matrix to perform swaps.
* **Space Complexity:**

  * **Python:** `O(1)` — Performed in-place.
  * **Java:** `O(n^2)` — Required to store the result in a new `ArrayList<ArrayList<Integer>>`.

## Self Learning

### Can it be improved? If yes, then how?

* **Java optimization:**
  If the problem permitted returning an `int[][]`, the space complexity could be reduced to `O(1)`.
* **Non-square matrices:**
  This in-place approach only works for square matrices (`n × n`). For rectangular matrices (`n × m`), a new matrix of size `m × n` is required, where:

  ```text
  new_mat[j][i] = old_mat[i][j]
  ```
* **Python alternative:**
  For very large matrices, `zip(*mat)` can be used to generate a transposed version, though it creates a new object instead of modifying in place.
