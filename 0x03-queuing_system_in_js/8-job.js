import { createQueue } from "kue";
const queue = createQueue();

function createPushNotificationsJobs(jobs, queue) {
    if ((Array.isArray(jobs))) {
        jobs.forEach(myjob => {
            const job = queue.create('push_notification_code_3', myjob).save((err) => {
                if (!err) {
                    console.log(`Notification job created: ${job.id}`);
                }
            });
            job.on('complete', function () {
                console.log(`Notification job ${job.id} completed`);
            });
            job.on('failed', function (err) {
                console.log(`Notification job ${job.id} failed: ${err}`);
            });
            job.on('progress', function (progress, data) {
                console.log(`Notification job ${job.id} ${progress}% complete`)
            });
        });
    } else {
        console.error('Jobs is not an array');
    }
}


module.exports = createPushNotificationsJobs;