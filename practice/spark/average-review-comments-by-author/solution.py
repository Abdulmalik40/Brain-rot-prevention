Author_df = repo_commits.alias("rc").join(code_reviews.alias("cr"), col("rc.author") == col("cr.author")  ,"inner").select("cr.author","comments","commit_at","review_id")

Author_df2 = Author_df.groupBy("author").agg(
                    avg("comments").alias("avg_commets"),
                    min("commit_at").alias("earliest_commit")
   )
