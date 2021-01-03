from JsonDB import JsonDB

db = JsonDB('Database')

class User(db.Model):
    
    __tablename__ = 'Users'
    
    name = db.Dict('Name')
    email = db.Dict('Email')
    fruits = db.List()
    
class Posts(db.Model):
    
    __tablename__ = "Posts"
    
    title = db.Dict("Title")
    content = db.Dict("Content", nullable=False)


# To create a Database run it once.
db.create_all()