#!/usr/bin/python3
import sys
import MySQLdb

db = MySQLdb.connect(host="localhost",port=3306,db="hbtn_0e_0_usa",read_default_file="~/.my.cnf")
#Use database, select all states
cur = db.cursor()


if __name__ == "__main__":

    cur.execute("SELECT * FROM `states` WHERE Name LIKE BINARY 'N%' ORDER BY states.id ASC")


    for state in cur.fetchall():
        print(state)

cur.close()
db.close()
#print(rows)
