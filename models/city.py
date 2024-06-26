#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

import os


stor_type = os.environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"

    if stor_type == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship(
            "Place", cascade="all, delete-orphan", backref="cities"
        )
    else:
        name = ""
        state_id = ""
