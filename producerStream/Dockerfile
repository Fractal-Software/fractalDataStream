FROM python:3

ADD twitter-producer.py /

RUN pip3 install tweepy confluent-kafka

WORKDIR /

CMD ["python3", "twitter-producer.py"]