const fs = require('fs')
var server = require('http').Server(app);
var http = require('http').Server(app);
var io = require('socket.io')(http);
var socketio_port = '33334';
const Promise = require('bluebird');
var app = require('express')();
const { Kafka, logLevel } = require('kafkajs');
const { exec } = require('child_process');

const kafka = new Kafka({
  logLevel: logLevel.INFO,
  brokers: ["kafka1:9093,kafka2:9094,kafka3:9095"],
  clientId: 'backend-consumer'//,
  //ssl: {
  //   rejectUnauthorized: false
  //},
  //sasl: {
  //  mechanism: 'plain',
  //  username: 'test',
  //  password: 'test123',
  //},
})

server.listen(44444); //for REST requests later
// WARNING: app.listen(80) will NOT work here!

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){ //have to bounce to ext for now

  //Venezuela:
  const consumer_sentVen = kafka.consumer({ groupId: 'sentVen-group' , fromOffset: 0})
  const run_sentVen = async () => {
    const sentVen_topic = 'sentVen'
    await consumer_sentVen.connect();
    await consumer_sentVen.subscribe({ topic: sentVen_topic });
    await consumer_sentVen.run({
        eachMessage: async ({ topic, partition, message }) => {
            socket.emit(sentVen_topic, `${message.value}`);
            socket.broadcast.emit('sentVen', `${message.value}`);
        },
    });
  }

  run_sentVen().catch(e => console.error(`[example/consumer_sentVen] ${e.message}`, e))

  //USA
  const consumer_sentUSA = kafka.consumer({ groupId: 'sentUSA-group' , fromOffset: 0})
  const run_sentUSA = async () => {
    const sentUSA_topic = 'sentUSA'
    await consumer_sentUSA.connect();
    await consumer_sentUSA.subscribe({ topic: sentUSA_topic });
    await consumer_sentUSA.run({
        eachMessage: async ({ topic, partition, message }) => {
            // console.log({
            //     key: message.key.toString(),
            //     value: message.value.toString(),
            //     headers: message.headers,
            // })
            socket.emit(sentUSA_topic, `${message.value}`);
            socket.broadcast.emit('sentUSA', `${message.value}`);
        },
    });
  }

  run_sentUSA().catch(e => console.error(`[example/consumer_sentUSA] ${e.message}`, e))

  //Rusia
  const consumer_sentRus = kafka.consumer({ groupId: 'sentRus-group' , fromOffset: 0})
  const run_sentRus = async () => {
    const sentRus_topic = 'sentRus'
    await consumer_sentRus.connect();
    await consumer_sentRus.subscribe({ topic: sentRus_topic });
    await consumer_sentRus.run({
        eachMessage: async ({ topic, partition, message }) => {
            // console.log({
            //     key: message.key.toString(),
            //     value: message.value.toString(),
            //     headers: message.headers,
            // })
            socket.emit(sentRus_topic, `${message.value}`);
            socket.broadcast.emit('sentRus', `${message.value}`);
        },
    });
  }

  run_sentRus().catch(e => console.error(`[example/consumer_sentRus] ${e.message}`, e))

  //China
  const consumer_sentChina = kafka.consumer({ groupId: 'sentChina-group' , fromOffset: 0})
  const run_sentChina = async () => {
    const sentChina_topic = 'sentChina'
    await consumer_sentChina.connect();
    await consumer_sentChina.subscribe({ topic: sentChina_topic });
    await consumer_sentChina.run({
        eachMessage: async ({ topic, partition, message }) => {
            // console.log({
            //     key: message.key.toString(),
            //     value: message.value.toString(),
            //     headers: message.headers,
            // })
            socket.emit(sentChina_topic, `${message.value}`);
            socket.broadcast.emit('sentChina', `${message.value}`);
        },
    });
  }

  run_sentChina().catch(e => console.error(`[example/consumer_sentChina] ${e.message}`, e))

  //Israel
  const consumer_sentIs = kafka.consumer({ groupId: 'sentIs-group' , fromOffset: 0})
  const run_sentIs = async () => {
    const sentIs_topic = 'sentIs'
    await consumer_sentIs.connect();
    await consumer_sentIs.subscribe({ topic: sentIs_topic });
    await consumer_sentIs.run({
        eachMessage: async ({ topic, partition, message }) => {
            // console.log({
            //     key: message.key.toString(),
            //     value: message.value.toString(),
            //     headers: message.headers,
            // })
            socket.emit(sentIs_topic, `${message.value}`);
            socket.broadcast.emit('sentIs', `${message.value}`);
        },
    });
  }

  run_sentIs().catch(e => console.error(`[example/consumer_sentIs] ${e.message}`, e))

  //Germany
  const consumer_sentGer = kafka.consumer({ groupId: 'sentGer-group' , fromOffset: 0})
  const run_sentGer = async () => {
    const sentGer_topic = 'sentGer'
    await consumer_sentGer.connect();
    await consumer_sentGer.subscribe({ topic: sentGer_topic });
    await consumer_sentGer.run({
        eachMessage: async ({ topic, partition, message }) => {
            // console.log({
            //     key: message.key.toString(),
            //     value: message.value.toString(),
            //     headers: message.headers,
            // })
            socket.emit(sentGer_topic, `${message.value}`);
            socket.broadcast.emit('sentGer', `${message.value}`);
        },
    });
  }

  run_sentGer().catch(e => console.error(`[example/consumer_sentGer] ${e.message}`, e))

  //Japan
  const consumer_sentJap = kafka.consumer({ groupId: 'sentJap-group' , fromOffset: 0})
  const run_sentJap = async () => {
    const sentJap_topic = 'sentJap'
    await consumer_sentJap.connect();
    await consumer_sentJap.subscribe({ topic: sentJap_topic });
    await consumer_sentJap.run({
        eachMessage: async ({ topic, partition, message }) => {
            // console.log({
            //     key: message.key.toString(),
            //     value: message.value.toString(),
            //     headers: message.headers,
            // })
            socket.emit(sentJap_topic, `${message.value}`);
            socket.broadcast.emit('sentJap', `${message.value}`);
        },
    });
  }

  run_sentJap().catch(e => console.error(`[example/consumer_sentJap] ${e.message}`, e))

  //Iran
  const consumer_Iran = kafka.consumer({ groupId: 'sentIran-group' , fromOffset: 0})
  const run_sentIran = async () => {
    const sentIran_topic = 'sentIran'
    await consumer_Iran.connect();
    await consumer_Iran.subscribe({ topic: sentIran_topic });
    await consumer_Iran.run({
        eachMessage: async ({ topic, partition, message }) => {
            // console.log({
            //     key: message.key.toString(),
            //     value: message.value.toString(),
            //     headers: message.headers,
            // })
            socket.emit(sentIran_topic, `${message.value}`);
            socket.broadcast.emit('sentIran', `${message.value}`);
        },
    });
  }

  run_sentIran().catch(e => console.error(`[example/consumer_Iran] ${e.message}`, e))

  //Brazil
  const consumer_sentBra = kafka.consumer({ groupId: 'sentBra-group' , fromOffset: 0})
  const run_sentBra = async () => {
    const sentBra_topic = 'sentBra'
    await consumer_sentBra.connect();
    await consumer_sentBra.subscribe({ topic: sentBra_topic });
    await consumer_sentBra.run({
        eachMessage: async ({ topic, partition, message }) => {
            // console.log({
            //     key: message.key.toString(),
            //     value: message.value.toString(),
            //     headers: message.headers,
            // })
            socket.emit(sentBra_topic, `${message.value}`);
            socket.broadcast.emit('sentBra', `${message.value}`);
        },
    });
  }

  run_sentBra().catch(e => console.error(`[example/consumer_sentBra] ${e.message}`, e))