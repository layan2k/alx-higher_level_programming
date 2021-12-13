#!/usr/bin/node

const data = parseInt(process.arg[2], 10);
if (isNaN(data))
{
    console.log("Not a number")
}
else{
    console.log(`My number: ${data}`);
}
