import psycopg2

from core_server.env import env


class CursorWrapper:
    """
    This is just a wrapper over psycopg2 cursor. This exists because we use
    named cursor which needs to be closed after each call to execute. Named
    cursor is used to prevent fetching of all rows. This also contains the
    original connection.

    The idea is to initialize with a cursor and a connection and override the
    execute function(which closes existing cursor and re-creates) and rest of
    the attributes are just the attributes of the cursor object. See
    `__getattr__` method below.
    """
    def __init__(self, cursor, connection):
        self.connection = connection
        self.cursor = cursor
        # TODO: find ways to close connection

    def __getattr__(self, name):
        if name == 'description':
            return self.cursor.description
        if name == 'execute':
            try:
                self.cursor.close()
            except Exception:
                pass
            else:
                self.cursor = self.connection.cursor(name='deepl_cursor')
            finally:
                return self.cursor.execute
        return getattr(self.cursor, name)


def connect_db():
    # before you need to create an ssh tunnel with the database (also need a
    # key) with a command like:
    # ssh -i PEM_PATH -N -L 5432:34.202.46.89:8432 ubuntu@54.173.1.227
    # we can access the db only thourgh an EC2 instances and not directly for
    # security reason.
    params = {
        "host": env('DEEP_DB_HOST'),
        "port": env('DEEP_DB_PORT'),
        "dbname": env('DEEP_DB_NAME'),
        "user": env('DEEP_DB_USER'),
        "password": env('DEEP_DB_PASSWORD'),
        "sslmode": "require",
    }
    connection = psycopg2.connect(**params)
    # Use named cursor to make it server side which allows for controlling the
    # fetch sizes
    cursor: psycopg2.cursor = connection.cursor(name='deepl_cursor')
    return CursorWrapper(cursor, connection)
    # return cursor


def cursor_fetch_iterator(cursor: CursorWrapper, size=2000, limit=None):
    """
    Just don't fetch everything from the server. Fetch in batches of `size`
    """
    count = 0
    while True:
        records = cursor.fetchmany(size)
        if not records:
            break
        for row in records:
            if limit is not None and count > limit:
                return
            yield row
            count += 1
