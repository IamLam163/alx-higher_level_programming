#!/usr/bin/python3

import MySQLdb
db = MySQLdb.connect(host="localhost",port=3306,db="hbtn_0e_0_usa",read_default_file="~/.my.cnf")

#Use database, select all states

cur = db.cursor()

#cur2 = db.cursor()


if __name__ == "__main__":

    cur.execute("USE `hbtn_0e_0_usa`")
    cur.execute("SELECT * FROM `states`")

    #[print(state) for state in cur.fetchall()]

    for state in cur.fetchall():
        print(state)

#print(rows)
