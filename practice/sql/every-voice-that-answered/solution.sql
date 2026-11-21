SELECT DISTINCT(reply_to) AS content_id,COUNT(DISTINCT(sender_id)) AS reporter_count
FROM chat_msgs
WHERE reply_to IS NOT NULL
GROUP BY msg_id
