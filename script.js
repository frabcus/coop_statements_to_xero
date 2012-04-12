#!/usr/local/bin/node

var csv = require('csv');

csv().fromStream(process.stdin);


