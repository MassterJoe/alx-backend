import redis from 'redis';
import { promisify } from 'util';


const client = redis.createClient({
    host: 'localhost',
    port: 6379,
});



client.on('connect', function (){
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});


const channelName = 'holberton school channel';

function publishMessage(message, time) {
    const timeInt = parseInt(time);
    setTimeout(() => {
        console.log(`About to send ${message}`);
        client.publish(channelName, message);
    }, timeInt);
   
}


publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
