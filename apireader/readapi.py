__author__ = 'azeal_000'
import requests
import sqlite3 as lite

#make connections to database
con = lite.connect('urfchampitems.db')

with con:
    print("found database")
    cur = con.cursor()
    #code created table DO NOT RUN IF YOU DONT WANT TO DELETE DB
    #cur.execute("DROP TABLE IF EXISTS Champs")
    #cur.execute("CREATE TABLE Champs(champid INT, ranking TEXT, winner TEXT, "
    #           "item0 INT,item1 INT,item2 INT,item3 INT,item4 INT,item5 INT,item6 INT )")
#CONNECT TO BUCKET #1428099300 1428270000
epocht = 1428297300
while epocht < 1428335072:
    print(epocht)
    beginapi = {'beginDate': epocht, 'api_key': "c73fb9af-146f-47fa-ac4f-c2b0f43ac35e"}
    r = requests.get('https://na.api.pvp.net/api/lol/na/v4.1/game/ids', params=beginapi)


    bucket = r.text

    #END BUCKET

    #CONNECT TO MATCHES
    i = 1
    while i+10 < len(bucket):
        currentmatch = bucket[i:i+10]
        matchapi = {'includeTimeline': 'True', 'api_key': "c73fb9af-146f-47fa-ac4f-c2b0f43ac35e"}

        r2 = requests.get('https://na.api.pvp.net/api/lol/na/v2.2/match/' + currentmatch, params=matchapi)

        match = r2.json()

        p = match['participants']
        for champ in p:
            champID = champ['championId']
            ranking = champ['highestAchievedSeasonTier']
            s = champ['stats']
            win = s['winner']
            item0 = s['item0']
            item1 = s['item1']
            item2 = s['item2']
            item3 = s['item3']
            item4 = s['item4']
            item5 = s['item5']
            item6 = s['item6']
            #print("INSERT INTO champs VALUES(" + champID + ", " + ranking + ", " + win + ", " + item0 + ", " + item1 + ", "
            #      + item2 + ", " + item3 + ", " + item4 + ", " + item5 + ", " + item6 + ", ")
            with con:
                cur.execute("INSERT INTO champs VALUES(" + str(champID) + ", \"" + ranking + "\", \"" + str(win) + "\", "
                            + str(item0) +
                            ", " + str(item1) + ", " + str(item2) + ", " + str(item3) + ", " + str(item4) + ", " + str(item5) +
                            ", " + str(item6)+")")

        i+=11
        #END MATCHES
    epocht += 300