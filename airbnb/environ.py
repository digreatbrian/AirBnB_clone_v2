import os
from .settings import ENV

DB_DEV_ENVIRON = {
    'HBNB_MYSQL_USER': 'hbnb_dev',
    'HBNB_MYSQL_PWD': 'hbnb_dev_pwd',
    'HBNB_MYSQL_HOST': 'localhost',
    'HBNB_MYSQL_DB': 'hbnb_dev_db',
    'HBNB_TYPE_STORAGE': 'db'
}

DB_TEST_ENVIRON = {
    'HBNB_MYSQL_USER': 'hbnb_dev',
    'HBNB_MYSQL_PWD': 'hbnb_dev_pwd',
    'HBNB_MYSQL_HOST': 'localhost',
    'HBNB_MYSQL_DB': 'hbnb_dev_db',
    'HBNB_TYPE_STORAGE': 'db'
}

def set_db_dev_environ():
    '''Making the dev environment'''
    for env_key in DB_DEV_ENVIRON:
        os.environ[env_key] = DB_DEV_ENVIRON.get(env_key)

def set_db_test_environ():
    '''Making the test environment'''
    for env_key in DB_TEST_ENVIRON:
        os.environ[env_key] = DB_DEV_ENVIRON.get(env_key)

def load_environ():
    '''Loads the environment variables if not set by default'''
    if ENV == "dev":
        if list(DB_DEV_ENVIRON.keys())[0] not in os.environ:
            set_db_dev_environ()
    else:
        if list(DB_TEST_ENVIRON.keys())[0] not in os.environ:
            set_db_test_environ()
