#!/usr/bin/python3
"""
Initializes the model package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE)

if storage_t == "db":
    from model.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from model.engine.db_storage import FileStorage
    storage = FileStorage()
storage.reload()
