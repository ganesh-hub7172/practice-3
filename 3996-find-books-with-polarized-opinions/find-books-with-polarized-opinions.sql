# Write your MySQL query statement below
WITH book_stats AS (
    SELECT
        book_id,
        COUNT(*) AS total_sessions,
        MAX(session_rating) AS highest_rating,
        MIN(session_rating) AS lowest_rating,
        SUM(CASE
                WHEN session_rating >= 4 OR session_rating <= 2
                THEN 1
                ELSE 0
            END) AS extreme_ratings
    FROM reading_sessions
    GROUP BY book_id
    HAVING COUNT(*) >= 5
       AND MAX(session_rating) >= 4
       AND MIN(session_rating) <= 2
)

SELECT
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.pages,
    (bs.highest_rating - bs.lowest_rating) AS rating_spread,
    ROUND(bs.extreme_ratings / bs.total_sessions, 2) AS polarization_score
FROM books b
JOIN book_stats bs
ON b.book_id = bs.book_id
WHERE bs.extreme_ratings / bs.total_sessions >= 0.60
ORDER BY polarization_score DESC,
         b.title DESC;