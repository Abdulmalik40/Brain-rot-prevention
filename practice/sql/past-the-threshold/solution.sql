SELECT u.user_id , COUNT(session_id) AS session_count
FROM users u 
JOIN user_sessions us
USING(user_id)
GROUP BY us.user_id
HAVING COUNT(session_id) > 3
