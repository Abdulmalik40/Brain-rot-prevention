# show reviewers merged request since 2025 
# show how many uniuqe repos reviewd
# how many of the reviews merged
# most recent reveiw 

year_filterd = code_reviews.filter(year(col("merged")) >= 2025  )
                            .groupBy(col("reviewer"))
                            .agg(
                              countDistinct(col("repo_name")).alias("repo_reviewd"),
                              count("status").alias("merged_reviews"),
                              max("opened_at").alias("latest_review_opened")
                       
                              )
