repo_commits.groupBy(trim(lower(col("author")))).agg(
             count(col("message")).alias("commit_count"),
             countDistinct(col("repo_name")).alias("repo_count")
  ).filter(col("commit_count") >= 24 ).select(col("trim(lower(author))").alias("author"),col("commit_count"),col("repo_count"))
