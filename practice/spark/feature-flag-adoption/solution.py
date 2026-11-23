feat_flags.groupBy("flag_name","enabled").agg(
          count("enabled").alias("flag_count")
  )
