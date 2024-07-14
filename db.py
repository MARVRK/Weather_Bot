from datetime import datetime
from sqlalchemy import Column,create_engine,Integer,Float,String,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import config

# Connect to the PostgreSQL database using SQLAlchemy ORM
database_url = f'mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}/{config.MYSQL_DATABASE}'
engine = create_engine(database_url)
Base = declarative_base()

class Weather(Base):
	__tablename__ = 'weather_data'
	id = Column(Integer, primary_key=True)
	temperature = Column(Float)
	humidity = Column(Integer)
	description = Column(String(150))
	feels_like = Column(Float)
	country = Column(String(150))
	town = Column(String(150))
	created_at = Column(DateTime, default=datetime.now)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()