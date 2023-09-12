#!/usr/bin/node
let process = require("process");
let args = process.argv;

let result = Number(args[2]);

if (isNaN(result))
{
	console.log("Not a number")
}
else
{
	console.log("My number: " + result);
}
