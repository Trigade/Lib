import sqlite3 as sq

#@classmethod    #Oluşturmadan kullanmaya yarıyor
#@staticmethod #Bir kez oluşturulduktan sonra Her yerden ulaşmaya yarıyor G4G
class DbService:
    def __init__(self,connStr):
        self.conn = sq.connect(connStr)
        
        self.__create_user_table()
        self.__create_book_table()
        self.__create_writer_table()
        
    def get_db(self):
        return self.conn
    
    def __create_user_table(self):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    user_name TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
                """
            )
    def __create_book_table(self):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS books(
                    id TEXT PRIMARY KEY,
                    book_name TEXT NOT NULL,
                    
                    added_by INTEGER NOT NULL,
                    writer_id TEXT NOT NULL,

                    FOREIGN KEY (added_by) REFERENCES users(id),
                    FOREIGN KEY (writer_id) REFERENCES writers(id)
                )
                """
            )
    def __create_writer_table(self):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS writers(
                    id TEXT PRIMARY KEY,
                    writer_name TEXT NOT NULL,
                )
                """
            )