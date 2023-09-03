import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
        'phoneNumber': '09159224216',
        'message': 'This is the code to verify your account'
      }

      
const job = queue.create('push_notification_code', jobData).save((err) => {
    if (!err) {
        console.log(`Notification job created ${job.id}`);
    }
});

job.on('complete', function () {
    console.log('Notification job completed');
});
job.on('failed', function () {
    console.log('Notification job failed');
});