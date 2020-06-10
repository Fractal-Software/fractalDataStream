FROM python:3

LABEL maintainer="kmillan"

RUN apt install librdkafka-dev
RUN pip install tweepy confluent-kafka

COPY twitter.py /
ENTRYPOINT ["cd","/"]
CMD ["python", "twitter-producer.py"]