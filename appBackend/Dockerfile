FROM node:10.15.2

WORKDIR /app

COPY backendConsumer.js /app
ENTRYPOINT ["cd","/app"]

WORKDIR / 

RUN npm install && \
    npm i express socket.io
EXPOSE 44444 33334
CMD npm start