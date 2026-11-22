SELECT DISTINCT to_date(start_at) AS run_date
FROM data_pipes
WHERE to_date(start_at) < DATE '2026-05-01'
ORDER BY run_date;
