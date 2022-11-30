#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];

  for (const i in list) {
    newlist.unshift(list[i]);
  }
  return (newlist);
};
