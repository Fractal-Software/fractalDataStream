# Sentiment Analysis Pipeline

Container Memory Size must be set to atleast 6G, for Ubuntu see:

https://hostadvice.com/how-to/how-to-limit-a-docker-containers-resources-on-ubuntu-18-04/

For mac and Windows this can be set on Docker > Preferences

This application was made for the purpose of creating a sentiment analysis pipeline that connects to twitter
-for a given subject-, and sends the processed data to the backend.

## Start the application:

Initialize docker swarm

```javascript
docker swarm init
```

The external secrets must be created before you deploy the docker-compose.yml file:

```javascript
$ echo "A secret content" | docker secret create consumer_key -
$ echo "A secret content" | docker secret create consumer_secret -
$ echo "A secret content" | docker secret create access_key -
$ echo "A secret content" | docker secret create access_secret -
```

## Build the image:

```javascript
$ docker-compose build
```

## Deploy the stack with docker stack:

```javascript
$ docker stack deploy -c docker-compose.yml fractal-pipeline
```