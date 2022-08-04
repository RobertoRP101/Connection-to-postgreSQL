from ConnectionDB.ConnectionDB import ConnectionDB
from logger_base import log


class PoolCursor(object):
    def __init__(self):
        self._cursor = None
        self._connection = None

    def __enter__(self):
        self._connection = ConnectionDB.get_connection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._connection.rollback()
            log.error(f'[ROLLBACK] Exception occured: {exc_val}, {exc_type}, {exc_tb}')
        else:
            self._connection.commit()
            log.info(f'[COMMIT]')
        self._cursor.close()
        ConnectionDB.release_connection(self._connection)
