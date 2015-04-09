import requests
import sqlite3 as lite
import generatelookup as lookup
from collections import Counter

con = lite.connect('urfchampitems.db')
champdict = {}

# TODO name this function
def thing(champID):
    # find all rows with that ID
    c = Counter()

    with con:
        print("found database")
        cur = con.cursor()

        sql = "SELECT item0, item1, item2, item3, item4, item5, item6  FROM champs WHERE champid = '%d' LIMIT 100" %champID
        if True:
        # try:
            # Execute the SQL command
            cur.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cur.fetchall()
            for row in results: # row = id, item1, item2, item 3..... item6
                #print "LN " , row
                for i in range(0, len(row)):
                    if row[i] != 0:
                        item = row[i]
                        c[item] +=1
                        # print "added",

        # except:
        #     print "Error: unable to fetch data"


    # keep frequency of items

    # return list of most frequent items
    return c.most_common(7)

def translate(array):
    #
    # for item in array:
    #     print item,
    #     print lookup.get_item(item(0))

    return [lookup.get_item(item[0]) for item in array]


def generatetable():
    # run thing once for every champion, make a static lookup dictionary
    champlist = lookup.maketable()
    #print champlist[62]
    for key, value in champlist.items():
        print value
        champdict[value]= translate(thing(key))
        print "name", value, "items", champdict[value]

#    lookup.pack(champdict, "champdict.api")


####### MAIN

print "Champion         Items"
generatetable()

