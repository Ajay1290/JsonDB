# JsonDB

The JSON based Database Engine.

## Getting Started 
```python
from JsonDB import JsonDB
```

Create a database object along with database name
```python
db = JsonDB('Database')
```

Create Database Structure via inherting Map class in your Model class
```python
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
```

To create a Database run it once.
```python
db.create_all()
```

Query database using get method
```python
# To get Profiles dictonary externally
profiles = db.get('Profiles')

# To get Profiles dictonary internally
profiles = db.get('Profiles').value
```

## Links

Website: https://ajaypatil0921.github.io/JsonDB \
Documentation: https://ajaypatil0921.github.io/JsonDB/documentation \
Code: https://github.com/AjayPatil0921/JsonDB \
Issue tracker: https://github.com/AjayPatil0921/JsonDB/issues

## Contributing

For guidance on setting up a development environment and how to make a contribution to JsonDB, see the contributing guidelines.

## License

© Ajay Patil 2020-present. Code released under the MIT license.