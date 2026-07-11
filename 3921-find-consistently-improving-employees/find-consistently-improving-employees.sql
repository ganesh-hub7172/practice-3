# Write your MySQL query statement below
WITH ranked AS (
    SELECT
        employee_id,
        review_date,
        rating,
        ROW_NUMBER() OVER (
            PARTITION BY employee_id
            ORDER BY review_date DESC
        ) AS rn
    FROM performance_reviews
),
last_three AS (
    SELECT
        employee_id,
        review_date,
        rating
    FROM ranked
    WHERE rn <= 3
),
reviews AS (
    SELECT
        employee_id,
        MIN(CASE WHEN seq = 1 THEN rating END) AS r1,
        MIN(CASE WHEN seq = 2 THEN rating END) AS r2,
        MIN(CASE WHEN seq = 3 THEN rating END) AS r3
    FROM (
        SELECT
            employee_id,
            rating,
            ROW_NUMBER() OVER (
                PARTITION BY employee_id
                ORDER BY review_date
            ) AS seq
        FROM last_three
    ) t
    GROUP BY employee_id
)

SELECT
    e.employee_id,
    e.name,
    (r3 - r1) AS improvement_score
FROM employees e
JOIN reviews r
ON e.employee_id = r.employee_id
WHERE r1 < r2
  AND r2 < r3
ORDER BY improvement_score DESC, name ASC;