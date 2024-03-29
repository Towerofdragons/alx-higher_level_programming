#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument safely.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

            db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

            cur = db.cursor()

            with db.cursor() as cur:
                cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id \
                                        = states.id ORDER BY cities.id ASC")
                states = cur.fetchall()

            if states is not None:
                for state in states:
                    print (state)


