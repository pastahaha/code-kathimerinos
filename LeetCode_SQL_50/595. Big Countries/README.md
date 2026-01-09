# Big Countries

**Problem Link:** [LeetCode - Big Countries](https://leetcode.com/problems/big-countries/)

**Problem Topics:** Database, Pandas, Data Filtering

**Problem Description:** A country is **big** if:
- It has an area of at least three million (i.e., $3,000,000$ $km^2$).
- It has a population of at least twenty-five million (i.e., $25,000,000$).

Write a solution to find the name, population, and area of the big countries.

**Problem Example Output:**
- **Input Table (World):**
| name         | continent | area    | population | gdp          |
|--------------|-----------|---------|------------|--------------|
| Afghanistan  | Asia      | 652230  | 25500100   | 20343000000  |
| Albania      | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria      | Africa    | 2381741 | 37100000   | 188681000000 |
- **Output:**
| name        | population | area    |
|-------------|------------|---------|
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |

---

### Pseudocode
1. Identify the source table/DataFrame named `World`.
2. Apply a filter with two conditions:
    - `area` $\ge 3,000,000$
    - `population` $\ge 25,000,000$
3. Use a logical **OR** operator to combine these conditions (a country is "big" if *either* is true).
4. Select the specific columns: `name`, `population`, and `area`.

---

### My PostgreSQL Solution Approach
- **Strategy:** I used a `SELECT` statement to pull the required columns and a `WHERE` clause with the `OR` operator to capture countries meeting either threshold.
- **Methods/Functions Used:**
    - `SELECT`: Chooses the specific attributes to display.
    - `WHERE`: Filters rows based on the defined criteria.
    - `OR`: Logical operator that returns true if at least one of the conditions is met.

### My Python (Pandas) Solution Approach
- **Strategy:** I used boolean indexing to filter the rows of the `world` DataFrame. By placing the conditions inside square brackets, Pandas creates a mask to identify the rows that satisfy the "big" criteria.
- **Methods/Functions Used:**
    - `|` (Bitwise OR): Used in Pandas for element-wise logical OR operations between boolean Series.
    - `df[['col1', 'col2']]`: Used to filter the DataFrame to return only the requested columns.

---

### Complexities of My Approach
- **Time Complexity:** - **SQL:** $O(n)$ where $n$ is the number of rows in the table.
    - **Pandas:** $O(n)$ as it performs a linear scan to evaluate the conditions for each row.
- **Space Complexity:** - **SQL:** $O(k)$ where $k$ is the number of "big" countries returned.
    - **Pandas:** $O(n)$ for the intermediate boolean mask, resulting in $O(k)$ for the final output DataFrame.

---

### Self Learning
**Can it be improved?**
The current logic is the most direct way to solve the problem. However, in SQL, there is an alternative using `UNION`.

**How?**
- **SQL UNION:** Sometimes, using `UNION` to combine two separate queries (one for area, one for population) can be faster if there are separate indexes on the `area` and `population` columns. This allows the database engine to use index scans for both parts.
- **Example:**
  ```sql
  SELECT name, population, area FROM World WHERE area >= 3000000
  UNION
  SELECT name, population, area FROM World WHERE population >= 25000000;