#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete',
                              backref='state')
    else:
        @property
        def cities(self):
            """ cities """
            from models import storage
            from models.city import City

            c_list = []
            c_dic = storage.all(City)

            for city in c_dic.values():
                if city.state_id == self.id:
                    c_list.append(city)
            return c_list
        
