user_sessions = user_sessions
                .withColumn("session_date",date_format(col("session_start"),"yyyy-MM-dd"))
                .groupBy("session_date").agg(
                  count("session_id").alias("total_sessions"),
                  countDistinct("user_id").alias("unique_users")
                  ).select("session_date","total_sessions","unique_users")
