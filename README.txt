This application was made for the purpose of creating a sentiment analysis pipeline that connects to twitter
-for a given subject-, and sends the processed data all the way up to the backend.

Initialize docker swarm

docker swarm init

The external secrets must be created before you deploy the docker-compose.yml file:

$ echo "A secret content" | docker secret create consumer_key -
$ echo "A secret content" | docker secret create consumer_secret -
$ echo "A secret content" | docker secret create access_key -
$ echo "A secret content" | docker secret create access_secret -

Build the image (docker stack ignores the build option so you must do it manually):

$ docker-compose build

Deploy the stack with docker stack:

$ docker stack deploy -c docker-compose.yml pipeline