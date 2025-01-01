#!/usr/bin/python3
"""Database storage engine"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Database stoorage Class"""

    __engine = None
    __session = None

    # Public instance methods
    def __init__(self):
        # Assuming the environment variables for the database connection are set
        db_user = os.getenv("HBNB_MYSQL_USER")
        db_pwd = os.getenv("HBNB_MYSQL_PWD")
        db_host = os.getenv("HBNB_MYSQL_HOST")
        db_db = os.getenv("HBNB_MYSQL_DB")

        # Create the database engine URL
        db_url = f"mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db_db}"

        # Create the engine and bind it to the session
        self.__engine = create_engine(db_url)
        # Create tables if they don't exist
        Base.metadata.create_all(self.__engine)

        # Use a scoped session to ensure that sessions are correctly managed
        db_session = scoped_session(sessionmaker(bind=self.__engine))
        self.__session = db_session()

    def all(self, cls=None):
        """Query on the current database session"""
        classes = {
            "State": State,
            "City": City,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
        }

        results = {}
        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls)
            if cls:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    results[key] = obj
        else:
            for class_name in classes:
                objs = self.__session.query(classes[class_name]).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    results[key] = obj
        return results

    def new(self, obj):
        """Add object to current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        session = scoped_session(session_factory)
        self.__session = session()
