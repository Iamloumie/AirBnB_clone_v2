#!/usr/bin/python3
"""City Module for HBNB project"""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"

    # SQLAlchemy attributes
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    places = relationship("Place", backref="city",
                          cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initialize city"""
        super().__init__(*args, **kwargs)
        if not kwargs.get("name"):
            raise ValueError("City name is required")
        if not kwargs.get("state_id"):
            raise ValueError("state_id is required")
