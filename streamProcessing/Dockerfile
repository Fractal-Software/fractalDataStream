FROM ubuntu:latest
FROM python:3.7-stretch
LABEL maintainer="masroorh"

# Install OpenJDK 8
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

# # Install Python
# RUN \
#     apt-get update && \
#     apt-get install -y python3 && \
#     apt-get install -y python3-pip
COPY requirements.txt  /
WORKDIR /

# Install python dependencies
RUN apt-get update
RUN pip3 install --upgrade setuptools
RUN pip3 install --default-timeout=100 future
RUN pip3 install -r requirements.txt
# RUN pip3 install numpy
# RUN pip3 install pyspark


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

# # Define default command
RUN spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5,com.johnsnowlabs.nlp:spark-nlp_2.11:2.4.5 --class com.inndata.StructuredStreaming.Kafka --master local[*] /kafka-pyspark-streaming.py