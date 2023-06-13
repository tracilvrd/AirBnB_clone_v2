#!/usr/bin/python3
"""This module instantiates a storage"""
import os
#from models.base_model import BaseModel
#from models.state import State
#from models.city import City
#from models.user import User
#from models.place import Place
#from models.amenity import Amenity
#from models.review import Review


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
