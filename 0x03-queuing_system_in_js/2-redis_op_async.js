import redis from 'redis';
import { promisify } from 'util';


const client = redis.createClient({
    host: 'localhost',
    port: 6379,
});

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);


client.on('connect', function (){
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {

    try {
        const value = await getAsync(schoolName);
            console.log(value);

    } catch (err) {
        console.error(err);
    }
    
    }



displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
