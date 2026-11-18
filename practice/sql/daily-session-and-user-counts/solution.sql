SELECT FORMAT(session_start,"yyyy-MM-dd") AS session_date,
        COUNT(session_id) total_sessions,
        COUNT(DISTINCT(user_id)) unique_users
FROM user_sessions
GROUP BY session_date
