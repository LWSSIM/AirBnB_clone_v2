#!/usr/bin/python3
"""sql db class for storage logic"""

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

import os


user = os.environ.get("HBNB_MYSQL_USER")
pwd = os.environ.get("HBNB_MYSQL_PWD")
host = os.environ.get("HBNB_MYSQL_HOST")
db = os.environ.get("HBNB_MYSQL_DB")
env = os.environ.get("HBNB_ENV")

class DBStorage:
    """Main class to handle ormand connection to db"""

    __engine = None
    __session = None
    Session = None

    def __init__(self) -> None:
        """init the engine + session"""
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@{host}/{db}", pool_pre_ping=True
           )
        if env == "test":
            md = MetaData()
            md.drop_all(self.__engine, checkfirst=False)

    def all(self, cls=None):
        """Query current db for all objs in cls"""
        from models.amenity import Amenity
        from models.city import City, Base
        from models.place import Place
        from models.review import Review
        from models.state import State, Base
        from models.user import User

        query_res = {}

        if cls is None:
            cls_to_query = [User, State, City, Amenity, Place, Review]
        else:
            cls_to_query = [cls]

        for name in cls_to_query:
            objs = self.__session.query(name).all()
            for obj in objs:
                key = f"{name.__name__}.{obj.id}"
                query_res[key] = obj
        return query_res

    def new(self, obj):
        """add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        """
        from models.amenity import Amenity
        from models.city import City, Base
        from models.place import Place
        from models.review import Review
        from models.state import State, Base
        from models.user import User

        Base.metadata.create_all(self.__engine)

        DBStorage.Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = DBStorage.Session()

