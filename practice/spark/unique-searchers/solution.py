search_queries = search_queries.agg(countDistinct(col("user_id")))
search_queries.show(n=5)
# countDistinct()
