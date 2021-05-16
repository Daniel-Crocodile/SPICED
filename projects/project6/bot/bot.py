import telegram
import requests
import time
import sqlalchemy
from sqlalchemy import create_engine

#bot = telegram.Bot(token='1698400226:AAGpAR1-SG-lRk68ASispbPzMY82LGTEYj8')
webhook_url = "https://t.me/joinchat/Abun2xHbt-dhZWIy"
time.sleep(100)
bot_news = []
while len(bot_news) < 30:
    pg = create_engine('postgresql://postgres:3377@postgresdb:5432/polarity_sent', echo=True) # connects to postgres

    # extract news
    text_query = '''
    SELECT text FROM polarity_sent;
    '''
    sent_query = '''
    SELECT sentiment FROM polarity_sent;
    '''

    text = list(pg.execute(text_query))
    sentiment = list(pg.execute(sent_query))

    for i, news in enumerate(text):
        if news[0] not in bot_news:            
            text = 'Maybe that will be of interest for you' + news[0] + 'Pepita, hallo :)'
            json_bot = {'text': text}
            requests.post(url=webhook_url, json = json_bot)
            bot_news.append(news[0])
            break
        else:
            continue

    time.sleep(70)

    