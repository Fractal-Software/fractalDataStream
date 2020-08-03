let express = require('express');
const socketIO = require('socket.io');
const http = require('http');
const app = express();
let server = http.createServer(app);
const port  = process.env.PORT || 44444;
let io = socketIO(server)

server.listen(port);

let kafka = require('kafka-node'),
    Consumer = kafka.Consumer,
    client = new kafka.KafkaClient({kafkaHost: 'kafka1:29092'}),
    consumer = new Consumer(
        client,
        [
            { topic: 'sentVen', partition: 1 }, { topic: 'sentUSA', partition: 1 },
            { topic: 'sentRus', partition: 1 }, { topic: 'sentChina', partition: 1 },
            { topic: 'sentIs', partition: 1 }, { topic: 'sentGer', partition: 1 },
            { topic: 'sentJap', partition: 1 }, { topic: 'sentIran', partition: 1 },
            { topic: 'sentBra', partition: 1 }
        ],
        {
            autoCommit: false
        }
    );

consumer.on('message', function (message) {
    if(message){
        request.post({url:'http://localhost:44444/send-to-socket', form: {key:message}}, function(err,httpResponse,body){ 
        if(err)
            console.log('error => ', err);
        else{
            console.log('body => ', body);
            }
        })    
    }
});

app.post('/send-to-socket', function(req, res){
	const data = req.body.key.value || "no data";
	io.emit('data', { data });
})
