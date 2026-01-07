# Recyclable and Low Fat Products

**Problem Link:** [LeetCode - Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/)

**Problem Topics:** Database, Pandas, Data Filtering

**Problem Description:** Write a solution to find the IDs of products that are both low fat and recyclable.

**Problem Example Output:**
- **Input Table (Products):**
| product_id | low_fats | recyclable |
|------------|----------|------------|
| 0          | Y        | N          |
| 1          | Y        | Y          |
| 2          | N        | Y          |
| 3          | Y        | Y          |
- **Output:**
| product_id |
|------------|
| 1          |
| 3          |

---

### Pseudocode
1. Access the table or DataFrame containing product information.
2. Apply a filter where the column `low_fats` is equal to 'Y'.
3. Apply a secondary filter where the column `recyclable` is equal to 'Y'.
4. Ensure both conditions are met simultaneously (AND logic).
5. Select and return only the `product_id` column.

---

### My PostgreSQL Solution Approach
- **Strategy:** I used a standard `SELECT` statement with a `WHERE` clause. The `AND` operator ensures that only rows meeting both specific criteria are returned.
- **Methods/Functions Used:**
    - `SELECT`: Used to specify which columns to retrieve.
    - `WHERE`: Used to filter records based on specific conditions.
    - `AND`: A logical operator that allows multiple conditions to be checked; both must be true for the row to be included.

### My Python (Pandas) Solution Approach
- **Strategy:** I utilized **Boolean Indexing** to filter the DataFrame. This is a vectorized operation in Pandas, making it highly efficient for large datasets compared to manual loops.
- **Methods/Functions Used:**
    - `products[...]`: Square bracket notation used for filtering rows.
    - `&` (Bitwise AND): In Pandas, when filtering DataFrames, the `&` operator is used to perform element-wise logical AND operations between two boolean series.
    - `result[["product_id"]]`: Used double brackets to return the result as a DataFrame rather than a Series.

---

### Complexities of My Approach
- **Time Complexity:** - **SQL:** $O(n)$ where $n$ is the number of rows (can be $O(\log n)$ if an index exists on the filtered columns).
    - **Pandas:** $O(n)$ as it must check each row in the DataFrame.
- **Space Complexity:**
    - **SQL:** $O(k)$ where $k$ is the number of matching rows returned.
    - **Pandas:** $O(n)$ in the worst case to store the boolean mask, though the final output is $O(k)$.

---

### Self Learning
**Can it be improved?**
The current logic is the standard and most efficient way to perform a basic filter.

**How?**
- **SQL Optimization:** If this query is run frequently on a massive table, adding a **Composite Index** on `(low_fats, recyclable)` would significantly speed up the search.
- **Pandas Performance:** For extremely large datasets, using `products.query("low_fats == 'Y' & recyclable == 'Y'")` can sometimes be slightly more readable, though boolean indexing is usually faster for standard operations.