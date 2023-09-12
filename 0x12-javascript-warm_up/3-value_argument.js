#!/usr/bin/node
let process = require("process");
let args = process.argv
let len = 0;
for (arg in args)
{
	len++;
}

if (len > 2)
{
	console.log(args[2]);
}
else
{
	console.log("No arguement");
}
