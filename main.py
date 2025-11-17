from Services.memberService import MemberService
from Services.dbService import DbService
from Services.authService import AuthService
from os import system

system("cls")

def main():
    
    db = DbService("library.db")
    member_service = MemberService()
    
    auth = AuthService(db)
    auth.login("Kaya","123")
main()
