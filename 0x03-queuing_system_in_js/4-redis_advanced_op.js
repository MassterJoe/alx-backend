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

client.hset('HolbertonSchools', 'Portland', '50',redis.print);
client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
client.hset('HolbertonSchools','New York', '20', redis.print);
client.hset('HolbertonSchools','Bogota', '20', redis.print);
client.hset('HolbertonSchools', 'Cali', '40', redis.print);
client.hset('HolbertonSchools', 'Bogota', '20', redis.print);

client.hgetall('HolbertonSchools', (err, value) => {
    if (err) {
        console.error(err);
    } 
    if (value) {
        console.log(value);
    }
});