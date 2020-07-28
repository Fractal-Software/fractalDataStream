#!/bin/bash

bin/spark-submit \
    --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.5.3,com.johnsnowlabs.nlp:spark-nlp_2.11:2.5.3 \
    --class com.inndata.StructuredStreaming.Kafka \
    --master spark://master:7077 /kafka-pyspark-streaming.py


