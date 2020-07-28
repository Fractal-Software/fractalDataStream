FROM python:3.7.6

# RUN apk update && apk add build-base

# RUN apk add --no-cache openssl

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

WORKDIR /


COPY twitter-producer.py /
COPY requirements.txt /

RUN pip install --upgrade pip && \
    pip install tweepy --upgrade && \
    pip install -r requirements.txt

# CMD ["dockerize", "-wait", "tcp://kafka1:9092", "-timeout", "20s","python", "twitter-producer.py"]