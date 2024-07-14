from sqlalchemy import create_engine
from config import config


database_url = f'mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}/{config.MYSQL_DATABASE}'
engine = create_engine(database_url)
connection = None
try:
    connection = engine.connect()
    print("Connected to the MySQL database")
except Exception as e:
    print(f"Failed to connect to the MySQL database, error: {e}")
finally:
    if connection:
        print("Closing the MySQL connection")
    connection.close()