#!/usr/bin/python3
import sys
from sys import argv
import MySQLdb

db = MySQLdb.connect(host="localhost",port=3306,db="hbtn_0e_0_usa",read_default_file="~/.my.cnf")
#db = MySQLdb.connect(user=sys.argv[1],password=sys.argv[2],database=sys.argv[3], port=3306)

#Use database, select all states
cur = db.cursor()


if __name__ == "__main__":

    cur.execute("SELECT * FROM `states` WHERE Name LIKE BINARY '{:s}' ORDER BY id ASC".format(argv[4]))


    for state in cur.fetchall():
            if state[1] == argv[4]:
                print(state)

cur.close()
db.close()
#print(rows)
