employee_metrics.select(col("metric_value")).distinct().orderBy(col("metric_value").desc()).show(n=5)
