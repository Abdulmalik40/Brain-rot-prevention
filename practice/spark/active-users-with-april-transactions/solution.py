## I need to join users , transactions -- > combined 
## Filter the joined april month
## see actived account completed at least one transaction
joined_df = (transactions.join(broadcast(users), on="user_id", how="inner")
                .select(col("transaction_date").cast("date"),"account_status","user_id")
)
dateFilter_df = joined_df.filter(
                  col("transaction_date").between("2026-04-01","2026-04-30") 
)
final_df = dateFilter_df.filter(col("account_status") == "active").agg(count_distinct("user_id"))
                            .withColumnRenamed("count(DISTINCT user_id)","active_users_with_transactions")
