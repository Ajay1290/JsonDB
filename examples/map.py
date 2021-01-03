from JsonDB import JsonDB

db = JsonDB('Database')

class Database(db.Map):

    map = {
        "Profiles":{
            "Popular":[],
            "Dead":[],
            "Non-Popular":[]
        },
        "My Profiles":{
            "Name": "",
            "Followers": 2500,
            "Following": 1000
        },
    }

# To create a Database run it once.
db.create_all()

# To get Profiles dictonary externally
profiles = db.get('Profiles')

# To get Profiles dictonary internally
profiles = db.get('Profiles').value
