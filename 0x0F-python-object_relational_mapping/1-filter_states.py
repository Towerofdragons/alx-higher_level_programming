#!/usr/bin/python3
"""
Script lists all states from database 'hbtn_0e_0_usa' starting with 'N'
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
        db = MySQLdb.connect(host ="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")

        states = cur.fetchall()
