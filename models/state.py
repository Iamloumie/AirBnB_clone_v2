#!/usr/bin/python3
"""State Module for HBNB project"""

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"

    # SQLAlchemy attributes
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """
        Getter attribute for FileStorage
        Returns list of City instances with the State_id equal to the current State.id
        """
        city_list = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
