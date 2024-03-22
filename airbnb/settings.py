#!/usr/bin/python3
""" settings module """
import os


STORAGE_ENGINES = {
    "filestorage": "models.engine.file_storage.FileStorage",
    "dbstorage": "models.engine.db_storage.DBStorage"
}

STORAGE_ENGINE = STORAGE_ENGINES["dbstorage"] if os.getenv('HBNB_TYPE_STORAGE') == 'db' else STORAGE_ENGINES["filestorage"]

FILE_MODELS_DIR = "models"
DB_MODELS_DIR = "models.db_models"

if STORAGE_ENGINE == STORAGE_ENGINES["dbstorage"]:
    MODELS_DIR = DB_MODELS_DIR
else:
    MODELS_DIR = FILE_MODELS_DIR
