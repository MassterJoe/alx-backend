import redis from 'redis';

const client = redis.createClient({
    host: 'localhost',
    port: 6379,
});


client.on('connect', function (){
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, value) => {
        if (err) {
            console.error(err);

        } 
        console.log(value);
    })
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
