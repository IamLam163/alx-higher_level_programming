#!/usr/bin/node

const arg = parseInt(process.argv.length);

function findbig (a, b) {
  return (b - a);
}

if (isNaN(arg) || arg <= 3) {
  console.log(0);
} else {
  console.log(process.argv.slice(2).sort(findbig)[1]);
}
