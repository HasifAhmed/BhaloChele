import sqlite3   #enable control of an sqlite database

DB_FILE="curbur.db"

db = sqlite3.connect(DB_FILE,check_same_thread=False) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def add_account(user, pswd):
	DB_FILE="curbur.db"

	db = sqlite3.connect(DB_FILE,check_same_thread=False) #open if file exists, otherwise create
	c = db.cursor()               #facilitate db ops

	c.execute("SELECT account_id FROM accounts")
	id = 0
	for thing in c:
		id = int(thing[0])
    c.execute("INSERT INTO {0} VALUES( {1}, '{2}', '{3}');".format("accounts", id+1, user, pswd))
    db.commit() #save changes
    db.close() #close database


def add_to_viewed_stories(acc_id, title):
    c.execute("INSERT INTO {0} VALUES( {1}, '{2}');".format('stories_viewable', acc_id, title))

def add_text(acc_id, title, text):
    add_to_viewed_stories(acc_id, title)
    c.execute("SELECT entry_id FROM {0}".format(title))
    entry_id = 0
    for thing in c:
        id = thing[0]
    c.execute("INSERT INTO {0} VALUES( {1}, '{2}');".format(title, entry_id+1, text))

def add_new_story(acc_id,title,text):
    add_to_viewed_stories(acc_id, title)
    c.execute("CREATE TABLE {0} ({1} INTEGER PRIMARY KEY, {2} TEXT UNIQUE);".format(title, "entry_id", "entry"))
    c.execute("INSERT INTO {0} VALUES( {1}, '{2}');".format(title, 0, text))

#add_account('a', 'a')
#add_account('b','b')
#add_new_story(0, 'story1', 'blah blah blah.')
#add_text(1, 'story1', 'halb halb halb.')
#==========================================================

db.commit() #save changes
db.close() #close database
