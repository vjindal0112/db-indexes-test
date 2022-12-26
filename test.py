from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from geoalchemy2 import Geography
import time


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  return "{0}:{1}:{2}".format(int(hours), int(mins), sec)


# Define variables DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
DB_USERNAME = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'
SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# ----- init sqlalchemy -----
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, query_cache_size=0)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
# ----- init sqlalchemy -----


class Author(Base):
  __tablename__ = 'authors'

  author_id = Column(Integer, primary_key=True)
  author_name = Column(String)
  country = Column(String)


class Book(Base):
  __tablename__ = 'books'

  book_id = Column(Integer, primary_key=True)
  author_id = Column(Integer)
  price = Column(Integer)
  edition = Column(Integer)


class Point(Base):
  __tablename__ = 'points'

  id = Column(Integer, primary_key=True)
  loc = Column(Geography('POINT'))


def time_for_join_query():

  start = time.time()

  for k in range(30):
    with Session.begin() as session:
      statement = select(Author, Book).filter_by(author_name="YASH").join(
        Book, Author.author_id == Book.author_id).limit(10000 + k)
      result = session.execute(statement).all()
      # print(result)
      # for x in result:
      #   print(
      #     f'ID: {x[0].author_id}, Author: {x[0].author_name}, Book ID: {x[1].book_id}, Price: {x[1].price}, Edition: {x[1].edition}')
  end = time.time()
  print(f'TIME TAKEN: {time_convert(end - start)}')

  # TIME TAKEN: 0:0:23.04693579673767 (without indexes)

  # TIME TAKEN: 0:0:10.022242069244385 (with indexes!)


def GIS_data_query():
  start = time.time()
  for k in range(50):
    with engine.connect() as conn:
      result = conn.execute(
        "SELECT * FROM points ORDER BY loc <-> point '(74.013, 40.711)' LIMIT 1000")
  end = time.time()
  print(f'TIME TAKEN: {time_convert(end - start)}')

  # TIME TAKEN: 0:0:8.040539979934692 (without index)

  # TIME TAKEN: 0:0:0.20955514907836914 (with index!)


GIS_data_query()
