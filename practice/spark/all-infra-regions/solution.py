deduplicated = infra_nodes.dropDuplicates()

solution = deduplicated.orderBy(col("region").asc()).select("region").distinct()
