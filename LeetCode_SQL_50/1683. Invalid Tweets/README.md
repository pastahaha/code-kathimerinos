# Invalid Tweets

**Problem Link:** [LeetCode - Invalid Tweets](https://leetcode.com/problems/invalid-tweets/)

**Problem Topics:** Database, Pandas, String Operations

**Problem Description:** Write a solution to find the IDs of the invalid tweets. A tweet is considered **invalid** if the number of characters used in the content of the tweet is strictly greater than 15.

**Problem Example Output:**
- **Input Table (Tweets):**
| tweet_id | content                          |
|----------|----------------------------------|
| 1        | Vote for Biden                   |
| 2        | Let us make America great again  |
- **Output:**
| tweet_id |
|----------|
| 2        |

---

### Pseudocode
1. Load the `Tweets` data.
2. For each row, calculate the length of the string in the `content` column.
3. Filter rows where the length is greater than 15.
4. Select and return the `tweet_id` for those filtered rows.

---

### My PostgreSQL Solution Approach
- **Strategy:** I used the built-in `length()` function to evaluate the character count of each tweet's content within the `WHERE` clause.
- **Methods/Functions Used:**
    - `length(string)`: A standard SQL function that returns the number of characters in a string.
    - `SELECT tweet_id`: Retrieves only the ID column as required by the problem.

### My Python (Pandas) Solution Approach
- **Strategy:** I accessed the string properties of the `content` column using the `.str` accessor. This allows me to apply string methods like `len()` to every element in the column efficiently.
- **Methods/Functions Used:**
    - `.str.len()`: A Pandas Series method that calculates the length of each string in the Series. This is preferred over a manual `apply(len)` because it is optimized for vectorized operations.
    - `df[['tweet_id']]`: Subsets the DataFrame to return the result in the expected table format.

---

### Complexities of My Approach
- **Time Complexity:** - **SQL:** $O(n)$ where $n$ is the number of rows, as the database must compute the length for every entry.
    - **Pandas:** $O(n)$ because `.str.len()` iterates through each string in the column.
- **Space Complexity:** - **SQL:** $O(k)$ where $k$ is the number of invalid tweets.
    - **Pandas:** $O(k)$ for the resulting DataFrame, plus a temporary $O(n)$ boolean mask during the filtering step.

---

### Self Learning
**Can it be improved?**
The current methods are the standard approaches for string length validation.

**How?**
- **Character vs. Byte Length:** In PostgreSQL, `length()` counts characters. If you were dealing with multi-byte characters (like emojis or specific languages) and needed the storage size instead, you would use `octet_length()`.
- **Constraint Implementation:** In a real-world database design, if you want to prevent invalid tweets from ever being saved, you could add a **CHECK Constraint** to the table: 
  `ALTER TABLE Tweets ADD CONSTRAINT check_len CHECK (length(content) <= 15);`
- **Pandas Performance:** For massive datasets where performance is critical, ensuring the `content` column is of type `string` rather than `object` can sometimes improve the speed of `.str` accessor methods.