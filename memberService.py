from member import Member

class MemberService:
    def create_user(self,user_name,password):
        return Member(user_name,password)

    def delete_user(self,user_name):
        pass
    