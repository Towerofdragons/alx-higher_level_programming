#!/usr/bin/node
function factorial (n) 
{
	  return  isNaN(n) ? 1 || n === 0: n * factorial(n - 1);
}

console.log(factorial(Number(process.argv[2])));
