#!/usr/bin/python3
"""New Database Engine"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """
    Database storage class using SQLAlchemy.
    """

    def __init__(self):
        """
        Initialize DBStorage with database connection parameters.
        """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Retrieve all objects of a specific class or all classes.
        """
        my_classes = (Amenity, City, Place, Review, State, User)
        objects = {}

        if cls is None:
            for cls in my_classes:
                query = self.__session.query(cls)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj

        return objects

    def new(self, obj):
        """
        Add an object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes to the database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the current database session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and create a new session.
        """
        Base.metadata.create_all(self.__engine)

        session_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_maker)()

    def close(self):
        """
        Close the current database session.
        """
        self.__session.close()
