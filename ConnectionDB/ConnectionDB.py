from logger_base import log
from psycopg2 import pool
import sys


class ConnectionDB(object):
    _DATABASE: str = 'DB_Person'
    _USERNAME: str = 'postgres'
    _PASSWORD: str = 'Rip55204'
    _DB_PORT: str = '5432'
    _HOST: str = '127.0.0.1'
    # Minimun and maximum of connections using a pool
    _MIN_CON: int = 1
    _MAX_CON: int = 5
    _pool: object = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    host=cls._HOST,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.info('Successful pool connection')
                return cls._pool
            except Exception as e:
                log.error(f'Pool connection error: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def get_connection(cls):
        connection = cls.get_pool().getconn()
        log.info(f'Got connection {connection}')
        return connection

    @classmethod
    def release_connection(cls, connection):
        cls.get_pool().putconn(connection)
        log.info(f'Connection realeased: {connection}\n')

    @classmethod
    def close_connection(cls):
        cls.get_pool().closeall()
