import requests
import pymongo
import time


connection = pymongo.MongoClient('mongodb')  
db = connection.news


while True:
     url = ('https://newsapi.org/v2/everything?'
       'q=Corona&'
       'apiKey=edb6b96c6d204f5793b98f0b6ad6bef0')
     parameters = {'pageSize': 10}
   
     nnews = requests.get(url, params=parameters).json()
     list_news = list(nnews)
     list_info = []
     for i in range(len(list_news)):
          info = list_news[i]['info']
          y = {'info': info}
          db.news.insert_many(y)


     time.sleep(377)
