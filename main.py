from member import Member
from memberService import MemberService
from dbService import DbService
from authService import AuthService
from os import system

system("cls")

def check_password(member:Member,user_name:str,password:int):
    if user_name == member.get_user_name() and password == member.get_password():
        return True
    return False

def main():
    
    db = DbService("library.db")
    member_service = MemberService()
    
    auth = AuthService(db)
    auth.login("Kaya","123")
main()
