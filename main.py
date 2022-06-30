import json
import sqlalchemy
import os
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
NAME_DB = os.getenv("NAME_DB")
DSN = f'postgresql://{LOGIN}:{PASSWORD}@localhost:5432/{NAME_DB}'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()


def init_db(session):
    with open('tests_data.json', 'r') as fd:
        data = json.load(fd)
        for record in data:
            model = {
                'publisher': Publisher,
                'shop': Shop,
                'book': Book,
                'stock': Stock,
                'sale': Sale
            }[record.get('model')]
            session.add(model(id=record.get('pk'), **record.get('fields')))
        session.commit()


def serch_publisher(name_id=None):
    for publisher in session.query(Publisher).all():
        if publisher.name == name_id:
            return print(publisher)
        elif name_id.isdigit() and int(name_id) == publisher.id:
            return print(publisher)
    else:
        print("Ни чего не нашлось")


if __name__ == "__main__":
    init_db(session)
    name_id = input("Ведите имя или id издателя: ")
    serch_publisher(name_id)
