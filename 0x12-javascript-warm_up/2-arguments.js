#!/usr/bin/node
const  process  = require("process");
let len = process.argv.length

if (len <= 2)
{
	console.log("No Arguement")
}
else if (len === 3)
{
	console.log("Arguement found");
}
else
{
	console.log("Arguements found");
}
