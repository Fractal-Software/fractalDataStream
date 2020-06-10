FROM ubuntu:18.04
LABEL maintainer="kmillan"

# Install OpenJDK 8
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

# Install Python
RUN \
    apt-get update && \
    apt-get install -y python python-dev python-pip python-virtualenv && \
    rm -rf /var/lib/apt/lists/*

# Install PySpark and Numpy
RUN \
    pip install --upgrade pip && \
    pip install numpy && \
    pip install pyspark

# Create Checkpoint directories
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

# Define working directory
WORKDIR /

COPY kafka-pyspark-streaming.py /

# Define default command
CMD spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5,com.johnsnowlabs.nlp:spark-nlp_2.11:2.4.5 --class com.inndata.StructuredStreaming.Kafka --master local[*] /kafka-pyspark-streaming.py