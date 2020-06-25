FROM python:3

COPY ["twitter-producer.py", "/"]

RUN pip install tweepy kafka-python

WORKDIR /

CMD ["python3", "twitter-producer.py"]