#!/usr/bin/node

const fs = require("fs");
const request = require("request");

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }

  body = JSON.parse(body);

  let todoObj = {};

  for (const todo of body) {
    const user = todo.userId;
    if (todoObj[user] === undefined) {
      todoObj[user] = 0;
    }
    if (todo.completed) {
      todoObj[user] += 1;
    }
  }

  console.log(todoObj);
});
