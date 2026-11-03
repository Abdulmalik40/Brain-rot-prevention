svc_health_1 = svc_health.groupBy(col("svc_name")).agg( count(col("check_id")).alias("check_count"))   

svc_health_1.orderBy(col("check_count").desc(),col("svc_name").asc())
