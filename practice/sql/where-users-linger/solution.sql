WITH appeared AS(
SELECT u.device_id,d.os_name,AVG(u.session_duration_sec)AS avg_duration
  FROM user_sessions AS u
  INNER JOIN devices AS d
  ON  u.device_id = d.device_id
  WHERE d.device_type = "mobile"
  GROUP BY d.os_name
  ORDER BY AVG(u.session_duration_sec) DESC

),
Ranked_os AS (
  SELECT *,RANK() OVER(ORDER BY avg_duration DESC) as flag
  FROM appeared
  )
SELECT os_name,avg_duration
FROM Ranked_os
WHERE flag = 1
