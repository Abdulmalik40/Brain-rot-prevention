products = products.dropna()
products.orderBy(col("rating"),col("product_name")).select("product_name","rating").show(n=10)
