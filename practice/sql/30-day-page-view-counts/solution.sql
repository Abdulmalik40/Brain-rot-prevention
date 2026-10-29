-- 1- TOTAL PAGE view
-- 2- 2025 up to 28 DECEMBER (28 december is included) = |  >
-- 3-count every view

SELECT user_id,COUNT(view_id) 
FROM page_views
WHERE viewed_at BETWEEN '2025-01-01' AND '2025-12-28'   
GROUP BY user_id
