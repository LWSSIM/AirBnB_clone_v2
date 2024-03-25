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
    """Main class to handle orm and connection to db"""

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

    def all(self, cls=None, id=None):
        """Query current db for all objs in cls"""
        from models.amenity import Amenity
        from models.city import City, Base
        from models.place import Place
        from models.review import Review
        from models.state import State, Base
        from models.user import User

        query_res = {}

        if cls is None:
            cls_to_query = [State, City, User, Amenity, Place, Review]
            res = []
            for name in cls_to_query:
                res.extend(self.__session.query(name).all())
        if id:
            res = self.__session.query(cls).get(id)
            if res is not None:
                key = f"{res.to_dict()['__class__']}.{res.id}"
                query_res[key] = res
                return query_res
        else:
            res = self.__session.query(cls).all()

        for obj in res:
            key = f"{obj.to_dict()['__class__']}.{obj.id}"
            query_res[key] = obj
        return query_res


    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def start_session(self):
        """a public instance method used for starting a new session"""
        self.__session = DBStorage.Session()

    def stop_session(self):
        """a public instance method used for ending a session"""
        self.save()
        self.__session.close()

    def reload(self):
        """create all tables in the database"""
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

    def close(self):
        """call close on the class Session"""
        self.__session.close()
