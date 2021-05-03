
import pymongo

connection = pymongo.MongoClient()
connection = pymongo.MongoClient('localhost')  # <-- could be container name

db = connection.students

db.vanilla.find_one()
ada = db.vanilla.find_one()

# objects are dictionaries
type(ada)
ada['name']

db.vanilla.find()
cursor = db.vanilla.find()

# convert to a list or loop over it or similar
entries = list(cursor)
entries[3]

list(cursor) # empty

cursor.retrieved
cursor

# also see: iterators and generators
db.vanilla.find_one({'name': 'Charlie'})
db.vanilla.find_one({'loc': {'$gt': 100}})
