# Write your MySQL query statement below
WITH weekly_meetings AS (
    SELECT
        employee_id,
        YEAR(meeting_date) AS yr,
        WEEK(meeting_date, 1) AS wk,
        SUM(duration_hours) AS total_hours
    FROM meetings
    GROUP BY employee_id, YEAR(meeting_date), WEEK(meeting_date, 1)
),
meeting_heavy AS (
    SELECT
        employee_id,
        COUNT(*) AS meeting_heavy_weeks
    FROM weekly_meetings
    WHERE total_hours > 20
    GROUP BY employee_id
    HAVING COUNT(*) >= 2
)

SELECT
    e.employee_id,
    e.employee_name,
    e.department,
    m.meeting_heavy_weeks
FROM employees e
JOIN meeting_heavy m
ON e.employee_id = m.employee_id
ORDER BY m.meeting_heavy_weeks DESC,
         e.employee_name ASC;