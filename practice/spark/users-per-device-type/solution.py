from pyspark.sql import functions as F

joined = user_sessions.join(devices, "device_id", "left")

result = joined.groupBy("device_type").agg(
  F.countDistinct(
    F.coalesce(F.col("user_id"), F.lit("__NULL__"))
  ).alias("user_count") 
)

result.show()
