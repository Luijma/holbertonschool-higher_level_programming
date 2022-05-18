#!/usr/bin/node
// computes number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log('code: ', error);
  } else {
    const completedTasks = {};
    const tasks = JSON.parse(body);

    for (let i = 0; i < tasks.length; ++i) {
      const userId = tasks[i].userId;
      const completed = tasks[i].completed;

      if (completed && !completedTasks[userId]) {
        completedTasks[userId] = 0;
      }

      if (completed) ++completedTasks[userId];
    }

    console.log(completedTasks);
  }
});
