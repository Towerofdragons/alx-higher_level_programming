#!/usr/bin/node
let args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) 
{
	  console.log(0);
} 
else 
{
	  
	argumentList = args.map(Number);
	arguementList.sort(function (a, b) { return b - a; });
	const ans = argumentList[1];
	console.log(ans);
}
