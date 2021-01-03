import os
import json
from .Models import Model, Map
from .Elements import List, Node, Dict
from .JsonObject import Get

class JsonDB:
    
    def __init__(self, name, path=None, _type="NoSQL"):
        self.name = name
        self.path = f"{os.getcwd()}\\{self.name}.json"
        if path:
            self.path = f"{path}\\{self.name}.json"
        self.db = self.load(self.path)
        self.type = _type
        self.Model = Model
        self.Map = Map
        self.List = List
        self.Node = Node
        self.Dict = Dict
        self.get = Get(self.db)
        
        
    def load(self, path):
        if os.path.exists(path):
            return self._load(path, 'r')
        return self._load(path, 'x')
        
    def _load(self, path, acc):
        if acc == 'x':
            try:
                open(path, acc).write("{}")
                return json.load(open(path,"r"))
            except:
                return json.load(open(path,"r"))
        return json.load(open(path, acc))
    
    def commit(self):
        try:
            json.dump(self.db , open(self.path, "w"))
            return True
        except Exception:
            return False
    
    def delete(self , key):
        if not key in self.db:
            return False
        else:
            del self.db[key]
            return True
    
    def clear(self):
        try:
            self.db.clear()
            return True
        except Exception:
            return False
    
    def create_all(self):
        self.clear()
        if self.type == "NoSQL":
            self.db = Map.harvest_map()
        else:
            nodes = Model.harvest_nodes()
            for node in nodes:
                l = list(node.items())
                for z in l:
                    self.db[z[0]] = [{}]
                    for s in z[1]:
                        self.db[z[0]][0][s[0]] = s[1]
        self.commit()