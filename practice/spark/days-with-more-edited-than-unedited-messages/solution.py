chat_msgs = chat_msgs.withColumn("sent_at2",date_format(col("sent_at"), "yyyy-MM-dd"))

w = Window.partitionBy("sent_at2")


result = chat_msgs.withColumn("edited_count",count( when( col ("edited") ==1,1 )).over(w))
                  .withColumn("non_edited_count",count(when( col("edited") != 1,1)).over(w))
                  .filter(col("edited_count")> col("non_edited_count")).orderBy("msg_id")
        
final = result.drop(["edited_count","non_edited_count","sent_at2"]).select("*")
