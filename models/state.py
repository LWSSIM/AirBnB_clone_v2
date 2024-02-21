#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

import os


stor_type = os.environ.get('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """State class"""

    if stor_type == 'db':
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """returns the list of City instances
            with the current State.id"""
            from models.__init__ import storage
            from models.city import City

            cur_cities = []
            all_objs = storage.all(City)

            for k, v in all_objs.items():
                if self.id == v.state_id:
                    cur_cities.append(v)

            return cur_cities
