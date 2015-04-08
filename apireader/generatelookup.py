import requests
import sqlite3 as lite
#import pickle
import json

# TODO make API calls to looks up champions by ID

champtable = {}
con = lite.connect('urfchampitems.db')



#
# def maketable():
#     with con:
#         print("found database")
#         cur = con.cursor()
#
#         sql = "SELECT * FROM champs"
#         try:
#             # Execute the SQL command
#             cur.execute(sql)
#             # Fetch all the rows in a list of lists.
#             results = cur.fetchall()
#             for row in results:
#                 id = row[0]
#                 # make API calls
#                 champs = {'api_key': "c73fb9af-146f-47fa-ac4f-c2b0f43ac35e"}
#                 r = requests.get('https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion/'+id, params=champs)
#                 dict = json.load(r)
#                 champtable[id]=dict[name]
#
#         except:
#             print "Error: unable to fetch data"
#     return champtable

def get_champ(number):

    champs = {'api_key': "c73fb9af-146f-47fa-ac4f-c2b0f43ac35e"}
    r = requests.get('https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion/'+str(number), params=champs)
    #print r.json()
    dict = r.json()

    return dict['name']


def get_item(number):

    items = {'api_key': "c73fb9af-146f-47fa-ac4f-c2b0f43ac35e"}
    r = requests.get('https://na.api.pvp.net/api/lol/static-data/na/v1.2/item/'+str(number), params=items)
    #print r.json()
    dict = r.json()

    return dict['name']

def testing():
    print "Trying to get champion 60 (Elise): ", get_champ(60)
    print "Trying to get item 1079 (Doran's Shield): ", get_item(1054)


def test(n1, n2):
    print "Trying to get champion",n1,":", get_champ(n1)
    print "Trying to get item", n2, ":", get_item(n2)
#
#
# def pack():
#     pickle.dump(champtable, open("lookup.table"))
#
#
# def unpack():
#     global champtable
#     champtable = pickle.load("lookup.table")

testing()
test(62, 3143)