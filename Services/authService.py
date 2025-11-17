class AuthService:
    def __init__(self,db):
        self.db = db
    def login(self,user_name,password):
        with self.db.get_db() as conn:
            query = f"SELECT user_name,password FROM users WHERE user_name = '{user_name}'"
            cursor = conn.cursor()
            cursor.execute(query)
            user = cursor.fetchone()
            
            if user[1] != password:
                raise Exception("Basarisiz")
            print("basarili")
            
            print(user)

    def register(self,user_name,password):
        with self.db.get_db() as conn:
            query = f"INSERT INTO users(user_name,password) values(?,?)"
            cursor = conn.cursor()
            cursor.execute(query,(user_name,password))