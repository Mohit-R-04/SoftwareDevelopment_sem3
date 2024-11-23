# database_manager.py

import oracledb

class DatabaseManager:
    _instance = None  # Singleton instance placeholder

    @staticmethod
    def get_instance(user=None, password=None, dsn=None):
        '''Retrieve or create the singleton instance of DatabaseManager'''
        if DatabaseManager._instance is None:
            DatabaseManager._instance = DatabaseManager(user, password, dsn)
        return DatabaseManager._instance

    def __init__(self, user, password, dsn):
        if DatabaseManager._instance is not None:
            raise Exception("This class is a singleton! Use `get_instance()` to get an instance.")
        self.user = user
        self.password = password
        self.dsn = dsn
        self.connection = None

    def __enter__(self):
        '''Context manager enter method to ensure connection is established'''
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        '''Context manager exit method to ensure connection is closed'''
        self.close()

    def connect(self):
        '''Establish a database connection if not already connected'''
        if not self.connection:
            self.connection = oracledb.connect(
                user=self.user,
                password=self.password,
                dsn=self.dsn
            )
            print("Database connection established.")

    def execute_query(self, query, commit=False):
        '''Executes a query and returns results for SELECT queries'''
        self.connect()
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            if commit:
                self.connection.commit()
            else:
                return cursor.fetchall()
        except oracledb.Error as e:
            print(f"Error executing query: {e}")
            if commit:
                self.connection.rollback()
        finally:
            cursor.close()

    def close(self):
        '''Close the database connection if open'''
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Database connection closed.")

# Command Pattern Implementation
class DatabaseCommand:
    '''Abstract base class for database commands'''
    def execute(self, db_manager):
        raise NotImplementedError("Each command must implement an execute method")

class SelectCommand(DatabaseCommand):
    def __init__(self, query):
        self.query = query

    def execute(self, db_manager):
        return db_manager.execute_query(self.query)

class InsertCommand(DatabaseCommand):
    def __init__(self, query):
        self.query = query

    def execute(self, db_manager):
        db_manager.execute_query(self.query, commit=True)

class UpdateCommand(DatabaseCommand):
    def __init__(self, query):
        self.query = query

    def execute(self, db_manager):
        db_manager.execute_query(self.query, commit=True)

class DeleteCommand(DatabaseCommand):
    def __init__(self, query):
        self.query = query

    def execute(self, db_manager):
        db_manager.execute_query(self.query, commit=True)
