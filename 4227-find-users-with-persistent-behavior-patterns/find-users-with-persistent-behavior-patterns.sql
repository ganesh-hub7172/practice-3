# Write your MySQL query statement below
WITH cte AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY user_id, action
               ORDER BY action_date
           ) AS rn
    FROM activity
),
groups_cte AS (
    SELECT *,
           DATE_SUB(action_date, INTERVAL rn DAY) AS grp
    FROM cte
),
streaks AS (
    SELECT
        user_id,
        action,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date,
        COUNT(*) AS streak_length
    FROM groups_cte
    GROUP BY user_id, action, grp
    HAVING COUNT(*) >= 5
),
ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY streak_length DESC
           ) AS rk
    FROM streaks
)

SELECT
    user_id,
    action,
    streak_length,
    start_date,
    end_date
FROM ranked
WHERE rk = 1
ORDER BY streak_length DESC, user_id ASC;