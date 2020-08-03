FROM node:10.15.2

WORKDIR /

COPY . /

RUN npm install && \
    npm i express socket.io

EXPOSE 44444 33334

CMD ["npm", "start"]