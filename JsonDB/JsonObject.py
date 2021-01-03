class Get:

	def __init__(self,db):
		self.db = db

	def _get(self,key):
		try:			
			return JsonObject(self.db, key, self.db[key])
		except Exception as e:			
			raise ValueError(f"No Key named {key} found.")

	def __call__(self,key):
		return self._get(key) 

class JsonObject(type({})):

	def __init__(self, db, key=None, value=None):		
		self.key = key
		self.value = value
		self.db = db
		self[key] = self.value
		if type(self.db) == type({}):
			self.db[key] = self.value
			self.get = Get(self.value)			