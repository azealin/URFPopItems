# URFPopItems
This project was created for the Riot API challenge from March 30th to April 15th
Justin Yang - AzeaIin
Anna Loukianova- Salabraithe

The idea of the project is simple, store and read the most commonly built items per champion, store it in a database.
This means I would be collecting data till the 13th, the last day of URF. Then my plan was to just create a fun champion
splashes with their favorite URF items and people can go to a simple front end website to select which champion they want to see.
This may mean that I would need a higher rate to pull games depending on how many total games there are.

Pulls are being done in python, front end html/css/js


TODO:
write python script to read db, db is urfchampitems.db, 
#make connections to database
con = lite.connect('urfchampitems.db')

with con:
    print("found database")
    cur = con.cursor()
	cur.execute("SQL STATEMENT HERE")

also need 
https://na.api.pvp.net/api/lol/na/
v1.2/champion/{id}

for the two calls

https://na.api.pvp.net/api/lol/na/
v1.2/item/{id}
