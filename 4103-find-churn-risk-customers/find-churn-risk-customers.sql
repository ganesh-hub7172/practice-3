# Write your MySQL query statement below
WITH last_event AS (
    SELECT
        user_id,
        event_type,
        plan_name,
        monthly_amount,
        event_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY event_date DESC, event_id DESC
        ) AS rn
    FROM subscription_events
),
user_stats AS (
    SELECT
        user_id,
        MIN(event_date) AS start_date,
        MAX(monthly_amount) AS max_historical_amount,
        SUM(event_type = 'downgrade') AS downgrade_count
    FROM subscription_events
    GROUP BY user_id
)

SELECT
    l.user_id,
    l.plan_name AS current_plan,
    l.monthly_amount AS current_monthly_amount,
    u.max_historical_amount,
    DATEDIFF(l.event_date, u.start_date) AS days_as_subscriber
FROM last_event l
JOIN user_stats u
ON l.user_id = u.user_id
WHERE l.rn = 1
  AND l.event_type <> 'cancel'
  AND u.downgrade_count >= 1
  AND l.monthly_amount < 0.5 * u.max_historical_amount
  AND DATEDIFF(l.event_date, u.start_date) >= 60
ORDER BY days_as_subscriber DESC,
         l.user_id ASC;