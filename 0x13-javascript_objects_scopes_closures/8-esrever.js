#!/usr/bin/node
exports.esrever = function(list) {
  const newlist = [];

  for (let i in list) {
    newlist.unshift(list[i]);
  }
  return (newlist);
}
