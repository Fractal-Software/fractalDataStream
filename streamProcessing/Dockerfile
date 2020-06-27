 
FROM bde2020/spark-base:2.4.5-hadoop2.7

ENV SPARK_MASTER_NAME spark-master
ENV SPARK_MASTER_PORT 7077

COPY submit.sh /

# Copy the requirements.txt first, for separate dependency resolving and downloading
ONBUILD COPY requirements.txt /app/
ONBUILD RUN cd /app \
      && pip3 install -r requirements.txt

# Copy the source code
ONBUILD COPY . /app

WORKDIR /

RUN \
  mkdir sparkCheckpointVen && \
  mkdir sparkCheckpointUSA && \
  mkdir sparkCheckpointRus && \
  mkdir sparkCheckpointChi && \
  mkdir sparkCheckpointIs && \
  mkdir sparkCheckpointGer && \
  mkdir sparkCheckpointJap && \
  mkdir sparkCheckpointIran && \
  mkdir sparkCheckpointBra

COPY kafka-pyspark-streaming.py /

CMD ["/bin/bash", "/submit.sh"]

# Define submit command
# CMD spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5,com.johnsnowlabs.nlp:spark-nlp_2.11:2.4.5 --class com.inndata.StructuredStreaming.Kafka --master local[*] /kafka-pyspark-streaming.py