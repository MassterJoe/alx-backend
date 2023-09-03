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
client.subscribe(channelName);
client.on('message', (channel, message) => {
    console.log(`${message}`);
    if (message === 'KILL_SERVER') {
        client.unsubscribe(channelName);
        console.log(`Unsubscribed from ${channelName}`);
        client.quit();
    }
});