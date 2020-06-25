FROM python:3

WORKDIR /

COPY twitter-producer.py /

RUN pip3 install tweepy confluent-kafka

WORKDIR /

CMD ["python3", "twitter-producer.py"]