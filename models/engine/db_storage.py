"""
Database storage system that uses sqlAlchemy
"""

from models.base_model import Base
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from sqlalchemy import create_engine
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
import os

CLASSES = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}



class DBStorage:
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the object"""
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(username, password, host, db),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """fetches all objects depending on the cls argument"""
        if not self.__session:
            self.reload()
        objs = {}
        if type(cls) == str:
            cls = CLASSES.get(cls, None)
        if cls:
            for obj in self.__session.query(cls):
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in CLASSES.values():
                for obj in self.__session.query(cls):
                    objs[obj.__class__.__name__ + '.' + obj.id] = obj
        return objs
    
    def reload(self):
        """reate all tables in the database"""
        sf = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sf)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)
