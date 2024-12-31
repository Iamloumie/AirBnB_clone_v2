#!/usr/bin/python3
"""Place Module for HBNB project"""

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.review import Review

# Define the place_amenity table for Many-To-Many relationship
place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    city_id = Column(
        String(60), ForeignKey("cities.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(
        String(60), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # For DBStorage
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    amenities = relationship(
        "Amenity", secondary="place_amenity", viewonly=False)
    city = relationship("City", back_populates="places")

    # For FileStorage
    amenity_ids = []

    @property
    def reviews(self):
        """Getter attribute for FileStorage returns list of reviews"""
        from models import storage

        all_reviews = storage.all(Review)
        return [review for review in all_reviews.values() if review.place_id == self.id]

    @property
    def amenities(self):
        """Getter attribute for FileStorage to return list of amenities"""
        from models import storage

        all_amenities = storage.all(Amenity)
        return [
            amenity
            for amenity in all_amenities.values()
            if amenity.id in self.amenity_ids
        ]

    @amenities.setter
    def amenities(self, obj):
        """Setter attribute for FileStorage that handles append for amenity_ids"""
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
