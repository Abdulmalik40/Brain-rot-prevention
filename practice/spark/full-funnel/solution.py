searchers = search_queries.select("user_id").distinct()
browsers = page_views.select("user_id").distinct()
buyers = transactions.select("user_id").distinct()


full_funnel_user_ids = searchers 
  .join(browsers, on="user_id", how="inner") 
  .join(buyers, on="user_id", how="inner")

result = full_funnel_user_ids 
  .join(users, on="user_id", how="inner") 
  .select("username") 
  .orderBy("username")
