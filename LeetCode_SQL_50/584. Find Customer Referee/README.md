# Find Customer Referee

**Problem Link:** [LeetCode - Find Customer Referee](https://leetcode.com/problems/find-customer-referee/)

**Problem Topics:** Database, Pandas, Data Filtering, Handling Null Values

**Problem Description:** Write a solution to report the names of the customers that are not referred by the customer with `id = 2`.

**Problem Example Output:**
- **Input Table (Customer):**
| id | name | referee_id |
|----|------|------------|
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
- **Output:**
| name |
|------|
| Will |
| Jane |
| Bill |
| Zack |

---

### Pseudocode
1. Access the `Customer` table or DataFrame.
2. Filter for rows where the `referee_id` is either:
    - Unknown/Empty (`NULL` or `NaN`).
    - Not equal to `2`.
3. Extract the `name` column from the filtered results.

---

### My PostgreSQL Solution Approach
- **Strategy:** The key challenge here is how SQL handles `NULL`. In SQL, `NULL != 2` results in `UNKNOWN`, not `TRUE`. Therefore, I explicitly used `IS NULL` combined with `OR` to ensure those customers are included.
- **Methods/Functions Used:**
    - `IS NULL`: Used to check for the absence of a value.
    - `!=`: The inequality operator.
    - `OR`: Logical operator used because a customer only needs to satisfy one of the two conditions to be included.

### My Python (Pandas) Solution Approach
- **Strategy:** Similar to SQL, Pandas requires explicit handling of missing data (`NaN`). I used the `.isna()` method to capture the null values and the bitwise OR operator for filtering.
- **Methods/Functions Used:**
    - `.isna()`: A Pandas method that returns a boolean mask identifying where values are missing.
    - `|` (Bitwise OR): Used for element-wise logical OR operations in Pandas filtering.
    - `!=`: Used to compare the Series values against the integer 2.

---

### Complexities of My Approach
- **Time Complexity:** - **SQL:** $O(n)$ where $n$ is the number of rows.
    - **Pandas:** $O(n)$ as every row must be evaluated against the boolean conditions.
- **Space Complexity:** - **SQL:** $O(k)$ for the resulting names.
    - **Pandas:** $O(n)$ to create the boolean masks before filtering.

---

### Self Learning
**Can it be improved?**
The logic is sound, but performance can be influenced by how nulls are stored.

**How?**
- **SQL Optimization:** In some databases, you could use `COALESCE(referee_id, 0) != 2`. This function replaces `NULL` with `0` (or any value other than 2) on the fly, allowing for a single comparison. However, the `OR` approach is often more readable and standard.
- **Handling NULLs:** This problem is a classic reminder that in data logic, **"Not 2"** does not automatically include **"Nothing"**. You must always account for three-valued logic (True, False, and Unknown/Null).