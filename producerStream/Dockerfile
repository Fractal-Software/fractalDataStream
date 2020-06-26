FROM python:3.7

COPY ["twitter-producer.py", "/"]

RUN pip install tweepy kafka-python

WORKDIR /

CMD ["python3", "twitter-producer.py"]