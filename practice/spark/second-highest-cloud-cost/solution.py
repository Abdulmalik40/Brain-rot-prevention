w1 = Window.orderBy(col("amount").desc())

answer = cloud_costs.withColumn("flag",
          dense_rank().over(w1)
  ).filter(col("flag") ==2).select(col("amount")).distinct()
