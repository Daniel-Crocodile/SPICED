
import os

password = os.getenv('POSTGRES_PASSWORD')
dbname = os.getenv('POSTGRES_DATABASE')

conn = f"postgresql://kristian:{password}@server:5432/{dbname}"

print(conn)

# sqlalchemy stuff