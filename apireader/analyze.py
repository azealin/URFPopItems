import requests
import sqlite3 as lite
import generatelookup as lookup
from collections import Counter

con = lite.connect('urfchampitems.db')
totals = Counter()
champdict1 = {}
champdict2 = {}
champdict3 = {}
champdict4 = {}
champdict5 = {}
champdict6 = {}
champdict7 = {}
totalgames1 = 0
totalgames2 = 0
totalgames3 = 0
totalgames4 = 0
totalgames5 = 0
totalgames6 = 0
totalgames7 = 0
# TODO name this function
def thing(champID):
    global totalgames1
    global totalgames2
    global totalgames3
    global totalgames4
    global totalgames5
    global totalgames6
    global totalgames7
    # find all rows with that ID
    c1 = Counter() # unranked
    c2 = Counter() #bronze
    c3 = Counter() #silver
    c4 = Counter() #gold
    c5 = Counter() #plat
    c6 = Counter() #diamond
    c7 = Counter() #master/challenger

    with con:
        #print("found database")
        cur = con.cursor()

        sql = "SELECT ranking, item0, item1, item2, item3, item4, item5, item6  FROM champs WHERE champid = '%d' " \
              % champID
        if True:
        # try:
            # Execute the SQL command
            cur.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cur.fetchall()
            for row in results: # row = id, item1, item2, item 3..... item6
                #print "LN " , row
                for i in range(1, len(row)):
                    if row[i] != 0:
                        ranking = row[0]

                        if ranking == 'UNRANKED':
                            item = row[i]
                            c1[item] += 1
                            if i == 1:
                                totalgames1 += 1
                        elif ranking == 'BRONZE':
                            item = row[i]
                            c2[item] += 1
                            if i == 1:
                                totalgames2 += 1
                        elif ranking == 'SILVER':
                            item = row[i]
                            c3[item] += 1
                            if i == 1:
                                totalgames3 += 1
                        elif ranking == 'GOLD':
                            item = row[i]
                            c4[item] += 1
                            if i == 1:
                                totalgames4 += 1
                        elif ranking == 'PLATINUM':
                            item = row[i]
                            c5[item] += 1
                            if i == 1:
                                totalgames5 += 1
                        elif ranking == 'DIAMOND':
                            item = row[i]
                            c6[item] += 1
                            if i == 1:
                                totalgames6 += 1
                        elif ranking == 'MASTER':
                            item = row[i]
                            c7[item] += 1
                            if i == 1:
                                totalgames7 += 1
                        elif ranking == 'CHALLENGER':
                            item = row[i]
                            c7[item] += 1
                            if i == 1:
                                    totalgames7 += 1
                        # print "added",
        # except:
        #     print "Error: unable to fetch data"

    # keep frequency of items

    # return list of most frequent items
    return [c1.most_common(10), c2.most_common(10), c3.most_common(10), c4.most_common(10), c5.most_common(10),
            c6.most_common(10), c7.most_common(10)]


def champranking(rank):
    global totals
    freq = Counter()
    print (rank)

    with con:
        #print("found database")
        cur = con.cursor()

        if isinstance(rank, tuple):
            #print %s, '\%s' %(rank[0] %rank[1])
            sql = "SELECT champid  FROM champs WHERE ranking in ( '%s', '%s')"\
            %(rank[0], rank[1])
        else:
            # print "pass"
            sql = "SELECT champid  FROM champs WHERE ranking = '%s' " \
              % rank

        cur.execute(sql)
        results = cur.fetchall()
        #print len(results)
        for row in results:
            try:
                #print row,
                champ = champdict[row[0]]
                #print champ
                freq[champ] += 1
                totals[champ] += 1
            except KeyError:
                continue

        return freq.most_common()




def translate(array):
    #
    # for item in array:
    #     print item,
    #     print lookup.get_item(item(0))

    return [(lookup.get_item(item[0]), item[1]) for item in array]


def generatetable():
    # run thing once for every champion, make a static lookup dictionary
    champlist = lookup.maketable()
    #print champlist[62[

    for key, value in champlist.items():
        #print value
        tally = thing(key)
        champdict1[value] = translate(tally[0])
        print("Table Unranked:\n Champion         Items")
        print(value, "\t", champdict1[value])

        champdict2[value] = translate(tally[1])
        print(value, "\t", champdict2[value])

        champdict3[value] = translate(tally[2])
        print(value, "\t", champdict3[value])

        champdict4[value] = translate(tally[3])
        print(value, "\t", champdict4[value])

        champdict5[value] = translate(tally[4])
        print(value, "\t", champdict5[value])

        champdict6[value] = translate(tally[5])
        print(value, "\t", champdict6[value])

        champdict7[value] = translate(tally[6])
        print(value, "\t", champdict7[value])

    #lookup.pack(champdict1, "champdict.api")


####### MAIN
# generatetable()
#
# print("Unranked: " + str(totalgames1) + " Bronze: " + str(totalgames2) + " Silver: " + str(totalgames3) +
#         " Gold: " + str(totalgames4) + " Platinum: " + str(totalgames5) + " Diamond: " + str(totalgames6) +
#         " Master/Challenger: " + str(totalgames7))
# print("Total Games " + str((totalgames1+totalgames2+totalgames3+totalgames4+totalgames5+totalgames6+totalgames7)/10))
print ("making table")
champdict = lookup.maketable()
print ("done")

ranks  = ["UNRANKED", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND", ("MASTER", "CHALLENGER")]

champranks = [champranking(r) for r in ranks]

for r in champranks:
    print (r)

print (totals.most_common())

