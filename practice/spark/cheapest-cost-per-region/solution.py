cloud_costs.groupBy("region").agg(min(col("amount")).alias("min_cost"))
