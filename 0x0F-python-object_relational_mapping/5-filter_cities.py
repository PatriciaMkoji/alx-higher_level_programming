#!/usr/bin/python3
""" lists all cities from db
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3], host="localhost", port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `c` \
    INNER JOIN `states` as `s` \
    ON `c`.`state_id` = `s`.`id`\
    ORDER BY `c`.`id`")
    print(", ".join([city[2] for city in c.fetchall()
                    if city[4] == sys.argv[4]]))
