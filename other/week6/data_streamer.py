from faker import Faker
import time
from sqlalchemy import create_engine

UNAME = "postgres"
PWD = "1234"
HOST = "my_postgres"
PORT = "5432"
DB = "postgres"

engine = create_engine(f"postgresql://{UNAME}:{PWD}@{HOST}:{PORT}/{DB}")
# the "trick" is that Docker-compose will know the host of the
# DB server simply by specifying the name of the service (my_postgres)

create_query = """
CREATE TABLE IF NOT EXISTS tweets (
    text TEXT
);
"""

engine.execute(create_query)

fake = Faker()

while True:
    fake_tweet = fake.text()

    engine.execute("""INSERT INTO tweets VALUES ('?') """, fake_tweet)
    print("Successfully inserted into DB!!!")

    time.sleep(3)