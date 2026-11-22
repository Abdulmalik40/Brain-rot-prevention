data_pipes.withColumn("run_date",to_date(col("start_at")))
            .filter(col("run_date") < lit("2026-05-1") )
              .select(col("run_date")).distinct()
