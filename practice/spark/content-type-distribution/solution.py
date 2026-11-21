content_items.groupBy("content_type").agg(
    count("content_type").alias("item_count")
  )
