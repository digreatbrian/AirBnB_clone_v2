STORAGE_ENGINES = {
    "filestorage": "models.engine.file_storage.FileStorage",
    "dbstorage": "models.engine.db_storage.DBStorage"
}
STORAGE_ENGINE = STORAGE_ENGINES["dbstorage"]

FILE_MODELS_DIR = "models"
DB_MODELS_DIR = "models.db_models"

ENV = "dev"

if STORAGE_ENGINE == STORAGE_ENGINES["dbstorage"]:
    MODELS_DIR = DB_MODELS_DIR
else:
    MODELS_DIR = FILE_MODELS_DIR
