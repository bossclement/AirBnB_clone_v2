#!/usr/bin/python3
import os

ts = os.getenv('HBNB_TYPE_STORAGE')


if ts == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()