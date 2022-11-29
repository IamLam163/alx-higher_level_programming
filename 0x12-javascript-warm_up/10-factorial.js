#!/usr/bin/node

const fact = parseInt(process.argv[2]);

function myfactorial (fact) {
  if (isNaN(fact) || fact === 0) {
    return (1);
  }
  return (fact * myfactorial(fact - 1));
}
console.log(myfactorial(fact));
