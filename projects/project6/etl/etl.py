import pymongo
import time
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb")

# Establish connection to Postgres
pg = create_engine('postgresql://postgres:3377@postgresdb:5432/polarity_sent', echo=True)

def get_mongo():
    db = client.news                  # Selects database 'news' in the MongoDB server
    collection = db.tweet_data        # Selects the collection 'data' 
    entries = collection.find(limit=12)
    return entries

def do_stuff(entries):
    s  = SentimentIntensityAnalyzer()
    news = []
    sent_num = []
    for e in entries:
        text = e['text']
        if text in news:
            sentiment = s.polarity_scores(e['text'])
            score = sentiment['compound']
            sent_num.append(score)
            news.append(text)
    return news, sent_num


def export(news):
    pg.execute('''
    CREATE TABLE IF NOT EXISTS polarity_sent (
    text VARCHAR(500),
    sentiment NUMERIC   
);
''')

while True:
    client = pymongo.MongoClient("mongodb")
    pg = create_engine('postgresql://postgres:3377@postgresdb:5432/polarity_sent', echo=True)
    export(do_stuff(get_mongo())) 
    time.sleep(30)  # seconds


