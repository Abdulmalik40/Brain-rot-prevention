chat_msgs = chat_msgs.dropna().dropDuplicates(["reply_to"])

chat_msgs.groupBy("reply_to").agg(
      countDistinct("sender_id").alias("reporter_count")
  ).select(col("reply_to").alias("content_id"),col("reporter_count"))
