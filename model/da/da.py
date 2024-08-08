from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from model.entity import *

connection_string = "mysql+pymysql://root:Aa79807980@localhost:3306/bank"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class DataAccess:
    def __init__(self, class_name):
        self.class_name = class_name

    def save(self, entity):
        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def edit(self, entity):
        session.merge(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def remove(self, id):
        entity = session.get(self.class_name, id)
        session.delete(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def find_all(self):
        entity_list = session.query(self.class_name).all()
        return entity_list

    def find_by_id(self, id):
        entity = session.get(self.class_name, id)
        if entity:
            return msg.showinfo("Data", f"ID {id} is found")
        else:
            return msg.showinfo("Data", f"Id {id} not found")

    def find_by(self, find_statement):
        entity = session.query(self.class_name).filter(find_statement).all()
        return entity