FROM python:3

ADD twitter-producer.py /

RUN pip install tweepy confluent-kafka

ENTRYPOINT ["cd","/"]
CMD ["python", "twitter-producer.py"]