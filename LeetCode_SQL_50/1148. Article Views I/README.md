# Article Views I

**Problem Link:** [LeetCode - Article Views I](https://leetcode.com/problems/article-views-i/)

**Problem Topics:** Database, Pandas, Data Cleaning

**Problem Description:** Write a solution to find all the authors that viewed at least one of their own articles. Return the result table sorted by `id` in ascending order.

**Problem Example Output:**
- **Input Table (Views):**
| article_id | author_id | viewer_id | view_date  |
|------------|-----------|-----------|------------|
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
- **Output:**
| id |
|----|
| 4  |
| 7  |

---

### Pseudocode
1. Load the `Views` dataset.
2. Filter the rows where the `author_id` is exactly the same as the `viewer_id`.
3. Select only the `author_id` column from these rows.
4. Remove any duplicate IDs (since an author might view multiple articles of their own).
5. Rename the column `author_id` to `id`.
6. Sort the resulting IDs in ascending order.

---

### My PostgreSQL Solution Approach
- **Strategy:** I used a simple `SELECT DISTINCT` to handle authors who viewed their own articles multiple times. The `WHERE` clause filters for the self-viewing condition, and `ORDER BY` ensures the output meets the sorting requirement.
- **Methods/Functions Used:**
    - `DISTINCT`: Removes duplicate rows from the result set.
    - `AS id`: Renames the output column to match the required schema.
    - `ORDER BY ... ASC`: Sorts the final list in ascending order.

### My Python (Pandas) Solution Approach
- **Strategy:** I chained several Pandas methods to achieve the result in a single logical block. First, I filtered the DataFrame, then subsetted the columns, removed duplicates, renamed the column, and finally sorted the values.
- **Methods/Functions Used:**
    - `views['author_id'] == views['viewer_id']`: A boolean comparison creating a mask.
    - `.drop_duplicates()`: Removes redundant rows.
    - `.rename(columns={...})`: Changes the column label.
    - `.sort_values(by='id')`: Sorts the DataFrame by the specified column.

---

### Complexities of My Approach
- **Time Complexity:** - **SQL:** $O(n \log n)$ due to the sorting (`ORDER BY`) and the unique check (`DISTINCT`).
    - **Pandas:** $O(n \log n)$ where $n$ is the number of rows, as sorting and dropping duplicates both carry this overhead.
- **Space Complexity:** - **SQL:** $O(k)$ where $k$ is the number of unique authors found.
    - **Pandas:** $O(n)$ in the worst case to hold the intermediate filtered DataFrame before dropping duplicates.

---

### Self Learning
**Can it be improved?**
The logic is efficient for a single table.

**How?**
- **Performance:** In very large databases, ensure there is an index on `author_id` and `viewer_id`.
- **Pandas Syntax:** You could also use `views.query("author_id == viewer_id")` for a cleaner, string-based syntax which can be slightly faster for certain engine configurations (like using `numexpr`).
- **Sorting:** Note that sorting is essential here; without the `ORDER BY` or `.sort_values()`, the solution would fail the judge's requirements even if the IDs were correct.