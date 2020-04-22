#!/usr/bin/python3
"""This is the new engine DBStorage"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class DBStorage:
    """DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """creates the engine
        """
        env_nm = os.environ.get('HBNB_ENV')
        user_nm = os.environ.get('HBNB_MYSQL_USER')
        passwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db_nm = os.environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user_nm, passwd, host, db_nm),
                                      pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if env_nm == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        """
        classes = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']
        objs = {}

        if cls is None:
            for class_nm in classes:
                query = self.__session.query(eval(class_nm)).all()
                for obj in query:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objs[key] = obj
        else:
            query = self.__session.query(eval(cls)).all()
            for obj in query:
                key = obj.__class__.__name__ + '.' + obj.id
                objs[key] = obj
        return objs

    def new(self, obj):
        """adds the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """call remove() method on the private session attr (self.__session)
        """
        self.__session.remove()
