from faker import Faker
import time
import pymongo
import logging

conn = pymongo.MongoClient('my_mongodb')
db = conn.students

fake = Faker()

open('out.txt', 'w').write('hello writing file\n')

while True:
    logging.critical('Python script is still alive : ' + time.asctime())
    logging.critical('hello world')
    name = fake.name()
    doc = {'name': name}
    db.vanilla.insert(doc)

    time.sleep(3)
