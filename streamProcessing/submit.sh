#!/bin/bash

export SPARK_MASTER_URL=spark://${SPARK_MASTER_NAME}:${SPARK_MASTER_PORT}
export SPARK_HOME=/spark

/wait-for-step.sh


/execute-step.sh
/spark/bin/spark-submit \
    --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5,com.johnsnowlabs.nlp:spark-nlp_2.11:2.4.5
    --class com.inndata.StructuredStreaming.Kafka
    --master spark://7077:7077 /kafka-pyspark-streaming.py

/finish-step.sh