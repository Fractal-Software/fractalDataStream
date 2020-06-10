FROM node:10.15.2

WORKDIR /app

COPY backendConsumer.js /app
ENTRYPOINT ["cd","/app"]
RUN npm install
EXPOSE 4444
CMD npm start