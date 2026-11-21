SELECT content_type , COUNT(content_type)
FROM content_items
GROUP BY content_type
