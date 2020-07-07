 
FROM bde2020/spark-base:2.4.5-hadoop2.7

ENV SPARK_MASTER_NAME spark-master
ENV SPARK_MASTER_PORT 7077

RUN apk add --no-cache openssl

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# COPY submit.sh /

# Copy the requirements.txt first, for separate dependency resolving and downloading
ONBUILD COPY requirements.txt /app/
ONBUILD RUN cd /app \
      && pip install -r requirements.txt

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
COPY submit.sh /
EXPOSE 8888 7077 8081

WORKDIR /

CMD ["dockerize", "-wait", "tcp://kafka1:9092", "-timeout", "10s", "/bin/bash", "/submit.sh"]


# CMD ["dockerize", "-wait", "tcp://kafka1:9092", "-timeout", "10s","spark-submit","--packages","org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5,com.johnsnowlabs.nlp:spark-nlp_2.11:2.4.5","--class com.inndata.StructuredStreaming.Kafka","--master spark://spark-master:7077","/kafka-pyspark-streaming.py"]
# Define submit command
# CMD spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5,com.johnsnowlabs.nlp:spark-nlp_2.11:2.4.5 --class com.inndata.StructuredStreaming.Kafka --master local[*] /kafka-pyspark-streaming.py