import pyspark
import os,sys,time
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession, SQLContext
from sparknlp.pretrained import PretrainedPipeline
import sparknlp
import json
from pyspark.sql.functions import regexp_replace
import pandas as pd
from pyspark.sql import functions as F
import pyspark.sql.types as T
import numpy as np
from pyspark.sql import Window

# Initiate spark context
spark = sparknlp.start()

pipeline = PretrainedPipeline('analyze_sentiment', lang='en')

# Define Schema
schema = T.StructType([ T.StructField("text", T.StringType(), True)])

# read stream from kafka producer
kafkaDf = spark \
        .readStream.format("kafka") \
        .option("kafka.bootstrap.servers","kafka-1:19092,kafka-2:29092,kafka-3:39092") \
        .option("subscribe", "tweetsTopic") \
        .load()

# transform stream for readability
dfx = kafkaDf.selectExpr("CAST(value AS STRING)") \
    .select(F.from_json('value', schema).alias('data')) \
    .filter("data.text != ''")  \
    .select('data.text')

# FILTER BY COUNTRY
df_Venezuela=dfx.filter(dfx.text.contains("Venezuela"))
df_USA=dfx.filter(dfx.text.contains("USA"))
df_Rusia=dfx.filter(dfx.text.contains("Rusia"))
df_China=dfx.filter(dfx.text.contains("China"))
df_Israel=dfx.filter(dfx.text.contains("Israel"))
df_Germany=dfx.filter(dfx.text.contains("Germany"))
df_Japan=dfx.filter(dfx.text.contains("Japan"))
df_Iran=dfx.filter(dfx.text.contains("Iran"))
df_Brazil=dfx.filter(dfx.text.contains("Brazil"))

def streaming_sent(dfX):
  # apply sentiment analysis to text stream
  df = pipeline.transform(dfX)

  # select sentiment column from pipeline output
  df = df.select('sentiment.result',"sentiment.metadata") \
      .withColumn('result',F.concat_ws(',','result')) \
      .withColumn("result", regexp_replace('result', "positive",'1')) \
      .withColumn("result", regexp_replace('result', "na",'0')) \
      .withColumn("result", regexp_replace('result', "negative",'-1')) \
      .select(F.split('result', ',').alias('sents'), 'metadata')

  # Convert datatypes
  mapper = F.udf(lambda x:[i['confidence'] for i in x], T.ArrayType(T.StringType()))
  df = df.withColumn("metadata", mapper('metadata'))
  df = df.withColumn("metadata", df.metadata.cast("array<float>"))

  # Compute column product
  df_product = df.withColumn("product",F.expr("transform(arrays_zip(sents, metadata), x -> x.sents * x.metadata)"))

  # Average array
  array_mean = F.udf(lambda x: float(np.mean(x)), T.FloatType())
  sent_df = df_product.select(array_mean("product").alias("value"))
  return sent_df

sent_Venezuela = streaming_sent(df_Venezuela)
sent_USA = streaming_sent(df_USA)
sent_Rusia = streaming_sent(df_Rusia)
sent_China = streaming_sent(df_China)
sent_Israel = streaming_sent(df_Israel)
sent_Germany = streaming_sent(df_Germany)
sent_Japan = streaming_sent(df_Japan)
sent_Iran = streaming_sent(df_Iran)
sent_Brazil = streaming_sent(df_Brazil)

# Write to console consumer
# sent1 = sent_Venezuela.writeStream \
#     .outputMode("append") \
#     .format("console") \
#     .option("truncate", False) \
#     .start()

# write to kafka topic
ds_Venezuela = sent_Venezuela \
  .selectExpr("CAST(value AS STRING) AS key", "to_json(struct(*)) AS value") \
  .writeStream \
  .outputMode("update") \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-1:19092,kafka-2:29092,kafka-3:39092") \
  .option("topic", "sentVen") \
  .option("checkpointLocation", "/sparkCheckpointVen") \
  .start() \

ds_USA = sent_USA \
  .selectExpr("CAST(value AS STRING) AS key", "to_json(struct(*)) AS value") \
  .writeStream \
  .outputMode("update") \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-1:19092,kafka-2:29092,kafka-3:39092") \
  .option("topic", "sentUSA") \
  .option("checkpointLocation", "/sparkCheckpointUSA") \
  .start() \

ds_Rusia = sent_Rusia \
  .selectExpr("CAST(value AS STRING) AS key", "to_json(struct(*)) AS value") \
  .writeStream \
  .outputMode("update") \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-1:19092,kafka-2:29092,kafka-3:39092") \
  .option("topic", "sentRus") \
  .option("checkpointLocation", "/sparkCheckpointRus") \
  .start() \

ds_China = sent_China \
  .selectExpr("CAST(value AS STRING) AS key", "to_json(struct(*)) AS value") \
  .writeStream \
  .outputMode("update") \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-1:19092,kafka-2:29092,kafka-3:39092") \
  .option("topic", "sentChina") \
  .option("checkpointLocation", "/sparkCheckpointChi") \
  .start() \

ds_Israel = sent_Israel \
  .selectExpr("CAST(value AS STRING) AS key", "to_json(struct(*)) AS value") \
  .writeStream \
  .outputMode("update") \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-1:19092,kafka-2:29092,kafka-3:39092") \
  .option("topic", "sentIs") \
  .option("checkpointLocation", "/sparkCheckpointIs") \
  .start() \

ds_Germany = sent_Germany \
  .selectExpr("CAST(value AS STRING) AS key", "to_json(struct(*)) AS value") \
  .writeStream \
  .outputMode("update") \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-1:19092,kafka-2:29092,kafka-3:39092") \
  .option("topic", "sentGer") \
  .option("checkpointLocation", "/sparkCheckpointGer") \
  .start() \

ds_Japan = sent_Japan \
  .selectExpr("CAST(value AS STRING) AS key", "to_json(struct(*)) AS value") \
  .writeStream \
  .outputMode("update") \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-1:19092,kafka-2:29092,kafka-3:39092") \
  .option("topic", "sentJap") \
  .option("checkpointLocation", "/sparkCheckpointJap") \
  .start() \

ds_Iran = sent_Iran \
  .selectExpr("CAST(value AS STRING) AS key", "to_json(struct(*)) AS value") \
  .writeStream \
  .outputMode("update") \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-1:19092,kafka-2:29092,kafka-3:39092") \
  .option("topic", "sentIran") \
  .option("checkpointLocation", "/sparkCheckpointIran") \
  .start() \

ds_Brazil = sent_Brazil \
  .selectExpr("CAST(value AS STRING) AS key", "to_json(struct(*)) AS value") \
  .writeStream \
  .outputMode("update") \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-1:19092,kafka-2:29092,kafka-3:39092") \
  .option("topic", "sentBra") \
  .option("checkpointLocation", "/sparkCheckpointBra") \
  .start() \
  .awaitTermination()


# Run the following command in the shell or terminal in order to initiate the consumer stream
# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5,com.johnsnowlabs.nlp:spark-nlp_2.11:2.4.5  --class com.inndata.StructuredStreaming.Kafka --master local[*] /home/kevin/dockerStream/streamProcessing/kafka-pyspark-streaming.py

# ds_USA = sent_USA \
#   .selectExpr("CAST(value AS STRING) AS key", "to_json(struct(*)) AS value") \
#   .writeStream \
#   .outputMode("update") \
#   .format("kafka") \
#   .option("kafka.bootstrap.servers", 'localhost:9092') \
#   .option("topic", "sentUSA") \
#   .option("checkpointLocation", "/home/kevin/dockerStream/streamProcessing/sparkCheckpointUSA") \
#   .start() \
#   .awaitTermination()