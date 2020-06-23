FROM python:3

LABEL maintainer="kmillan"

RUN pip install tweepy confluent-kafka

COPY twitter-producer.py /
ENTRYPOINT ["cd","/"]
CMD ["python", "twitter-producer.py"]