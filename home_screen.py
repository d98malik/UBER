class WelcomeScreen:
    def __init__(self,type:str):
        self.create_account = 1
        self.type = type
        self.login = 2
        self.option = None
        pass

    def welcome_msg(self):
        print(f"*********Welcome to the uber {self.type} app******")
        print("*********Please chosse your option***********")
        print("1.Create Account \n2.Login ")

        self.option = int(input())
        assert self.option in [1,2], print(f"invalid option selected {self.option}")
        print(f"option selected: {self.option}")
        return None

