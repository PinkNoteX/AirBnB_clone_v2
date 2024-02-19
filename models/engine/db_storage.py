#!/usr/bin/python3
""" db """
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

classes = {"City": City,
           "State": State,
           "Place": Place,
           "User": User,
           "Review": Review,
           "Amenity": Amenity}


class DBStorage:
    """ handle database engine """

    __engine = None
    __session = None

    def __init__(self):
        """ init """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all """
        dic = {}
        quary = []
        if cls:
            for name, value in all_classes.items():
                if name == cls:
                    quary = self.__session.query(value)
                    for ob in quary:
                        key = name + '.' + ob.id
                        dic[key] = ob
            return dic
        else:
            for name, value in all_classes.items():
                query = self.__seesion.query(value)
                for ob in query:
                    key = name + ob.id
                    dic[key] = ob
        return dic

    def new(self, obj):
        """ new """
        self.__session.add(obj)

    def save(self,obj):
        """ save """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete """
        self.__session.delete(obj)

    def reload(self):
        """ reload """
        Base.metadata.create_all(self.__engine)
        session_m = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session_scoped = scoped_session(session_m)
        self.__session = session_scoped()

    def close(self):
        """ close """
        self.__session.close()
