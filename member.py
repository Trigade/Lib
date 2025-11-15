class Member:
    def __init__(self,user_name,password):
        self.__user_name = user_name
        self.__password = password
        
    def get_user_name(self):
        return self.__user_name
    
    def get_password(self):
        return self.__password
    
    def set_user_name(self,new_user_name):
        self.__user_name = new_user_name
        
    def set_password(self,new_password):
        self.__password = new_password    
