#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

import os

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if "HBNB_TYPE_STORAGE" in os.environ.keys() and \
        os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
