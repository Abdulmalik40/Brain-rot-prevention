joined = users.join(broadcast(user_sessions),"user_id","inner")

joined.groupBy("user_id").agg(
              count("session_id").alias("session_count")
  ).filter(col("session_count") > 3 )
