content_items = content_items.dropna(subset="duration_seconds")
w = Window.partitionBy("content_type").orderBy(col("duration_seconds").desc())

content_items.withColumn("Longest",rank().over(w))
                                  .filter(year(col("publish_date")) >= 2026)
                                  .filter(col("Longest")==1)
                                  .select("content_id","title").distinct()
                                    .orderBy("content_id")
