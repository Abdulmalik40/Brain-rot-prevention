devices = devices.filter(col("device_type").isin("desktop","tablet","smart_tv"))

joined = user_sessions.join(devices,"device_id","inner")

changed = joined.withColumn("session_date", col("session_start").cast("date"))


changed
  .groupBy("session_date").agg(
    countDistinct(col("user_id"))
  )
