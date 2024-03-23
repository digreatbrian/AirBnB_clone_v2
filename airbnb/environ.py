#!/usr/bin/python3
""" environment tools """
import os


DB_DEV_ENVIRON = {
    'HBNB_MYSQL_USER': 'hbnb_dev',
    'HBNB_MYSQL_PWD': 'hbnb_dev_pwd',
    'HBNB_MYSQL_HOST': 'localhost',
    'HBNB_MYSQL_DB': 'hbnb_dev_db',
    'HBNB_TYPE_STORAGE': 'db'
}

DB_TEST_ENVIRON = {
    'HBNB_MYSQL_USER': 'hbnb_test',
    'HBNB_MYSQL_PWD': 'hbnb_test_pwd',
    'HBNB_MYSQL_HOST': 'localhost',
    'HBNB_MYSQL_DB': 'hbnb_test_db',
    'HBNB_TYPE_STORAGE': 'db'
}


def env_vars_set_properly():
    '''checks if all the necessary environment variables are set
    ```
    These include:
        HBNB_MYSQL_USER
        HBNB_MYSQL_PWD
        HBNB_MYSQL_HOST
        HBNB_MYSQL_DB
        HBNB_TYPE_STORAGE
    ```
    '''
    set_correct = True

    # use test env as default if an erro
    for key in DB_TEST_ENVIRON.keys():
        if not os.getenv(key):
            set_correct = False
            return set_correct
    return set_correct


def set_default_db_dev_environ():
    '''Making the default dev environment'''
    for env_key in DB_DEV_ENVIRON:
        os.environ[env_key] = DB_DEV_ENVIRON.get(env_key)


def set_default_db_test_environ():
    '''Making the default test environment'''
    for env_key in DB_TEST_ENVIRON:
        os.environ[env_key] = DB_DEV_ENVIRON.get(env_key)


def load_environ():
    '''Loads the environment variables if not set by default'''
    if 'HBNB_TYPE_STORAGE' not in os.environ and \
            not os.getenv("HBNB_TYPE_STORAGE") == 'db':
        # obviously lets use filestorage as default if not set
        # nothing else to do
        os.environ['HBNB_TYPE_STORAGE'] = 'file'
    else:
        # if set
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            if not env_vars_set_properly():
                err = """
                Environment variables not set correctly required
                vars include
                [HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST,
                  HBNB_MYSQL_DB, HBNB_TYPE_STORAGE]
                """.replace("\n", " ")
                raise TypeError(err)
