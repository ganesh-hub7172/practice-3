# Write your MySQL query statement below
WITH cte AS (
    SELECT *,
           FIRST_VALUE(score) OVER (
               PARTITION BY student_id, subject
               ORDER BY exam_date
           ) AS first_score,

           FIRST_VALUE(score) OVER (
               PARTITION BY student_id, subject
               ORDER BY exam_date DESC
           ) AS latest_score,

           ROW_NUMBER() OVER (
               PARTITION BY student_id, subject
               ORDER BY exam_date DESC
           ) AS rn,

           COUNT(*) OVER (
               PARTITION BY student_id, subject
           ) AS cnt
    FROM Scores
)

SELECT
    student_id,
    subject,
    first_score,
    latest_score
FROM cte
WHERE rn = 1
  AND cnt >= 2
  AND latest_score > first_score
ORDER BY student_id, subject;