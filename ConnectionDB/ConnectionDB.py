from logger_base import log
import psycopg2
import sys


class ConnectionDB(object):
    _DATABASE: str = 'DB_Person'
    _USERNAME: str = 'postgres'
    _PASSWORD: str = 'Rip55204'
    _DB_PORT: str = '5432'
    _HOST: str = '127.0.0.1'
    _connection_db = None
    _cursor = None

    @classmethod
    def getConnection(cls):
        if cls._connection_db is None:
            try:
                cls._connection_db = psycopg2.connect(
                                    user=cls._USERNAME,
                                    password=cls._PASSWORD,
                                    host=cls._HOST,
                                    port=cls._DB_PORT,
                                    database=cls._DATABASE
                )
                log.debug('Successful connection')
                return cls._connection_db
            except Exception as e:
                log.debug(f'Connection error: {e}')
                sys.exit()
        else:
            return cls._connection_db

    @classmethod
    def getCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.getConnection().cursor()
                log.debug(f'Successful cursor')
                return cls._cursor
            except Exception as e:
                log.debug(f'Cursor error: {type(e)}')
                sys.exit()
        else:
            return cls._cursor
