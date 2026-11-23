week_columns = (
  ci_builds
  .filter(col("status").isin("success", "failed", "canceled"))
  .filter(year(to_date(col("built_at"))) == 2026)
  .withColumn("week_start",
    date_sub(to_date(col("built_at")), dayofweek(to_date(col("built_at"))) - 1)
  )
)

week_columns.groupBy("week_start").agg(
  count(when(col("status") == "success", 1)).alias("success_count"),
  count(when(col("status") == "failed", 1)).alias("failed_count"),
  count(when(col("status") == "canceled", 1)).alias("canceled_count")
).orderBy("week_start")
