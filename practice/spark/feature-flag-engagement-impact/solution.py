from pyspark.sql import functions as F

# 1. Flags: small table (500 rows). Parse dates and build the 30-day window.
flags = (
  spark.table("feat_flags")
  .select(
    "flag_id",
    "flag_name",
    F.regexp_replace("flag_name", "_", " ").alias("display_name"),
    (F.col("enabled") == 1).alias("is_enabled"),
    F.to_timestamp("created").alias("window_start"),
  )
  .withColumn("window_end", F.col("window_start") + F.expr("INTERVAL 30 DAYS"))
)

# 2. Sessions: huge table (70M rows). Keep only the columns we need.
sessions = (
  spark.table("user_sessions")
  .select("session_id", F.to_timestamp("session_start").alias("session_ts"))
)

# 3. Count sessions per flag: inner join with the SMALL table broadcast.
counts = (
  sessions.join(
    F.broadcast(flags.select("flag_id", "window_start", "window_end")),
    on=(F.col("session_ts") >= F.col("window_start"))
     & (F.col("session_ts") <  F.col("window_end")),
    how="inner",
  )
  .groupBy("flag_id")
  .agg(F.count("session_id").alias("sessions_30d"))
)

# 4. Left-join counts back onto ALL flags, so zero-session flags appear.
result = (
  flags.join(counts, on="flag_id", how="left")
  .select(
    "flag_name",
    "display_name",
    "is_enabled",
    F.coalesce("sessions_30d", F.lit(0)).alias("sessions_30d"),
  )
  .orderBy("flag_name")
)

result.show(truncate=False)
