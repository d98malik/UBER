from home_screen import WelcomeScreen
from pymongo import MongoClient
import yaml

class Account:
    def __init__(self,type:str):
        """
        This is the account class. Handles login and account creation.
        """
        assert type in ["driver","customer"], print("invalid type")

        client = MongoClient("mongodb://localhost:27017") # type: ignore
        self.db = client["uber_clone"] # type: ignore
        w = WelcomeScreen(type)
        w.welcome_msg()
        
        if type == "driver": 
            self.userDb = self.db["drivers"]
        else:
            self.userDb = self.db["customers"]
  
        #to create account or login
        if w.option == w.create_account:
            self.create_account()
        elif w.option == w.login:
            self.login()
        else:
            raise Exception("unexpected value of option recieved")
        self.user_doc = None
    
    def create_account(self):
        """
        This method is used to create account for the user.
        """

        print("We are glad to see you here. It won't take more than a minute to onboard you.")

        user_doc = self._info_seeker()
        
        try:
            self.userDb.insert_one(user_doc) # type: ignore
        except:
            print("id was already present. Over writting it.")
            self.userDb.replace_one({"_id": user_doc["_id"]},user_doc) # type: ignoreuser_id},user_doc) #type: ignore

        self.user_doc = user_doc
        
        print("account created successfully. You can now login.\n\n\n")
        self.login()

        return None
    
    def _info_seeker(self):
        """to be replaced by child method"""
        return NotImplementedError

    def login(self):
        print("Welcome to login screen.")
        status = str("attempting login")
        login_attempts = 0
        while status=="attempting login" and (login_attempts<5):
            login_attempts+=1
            
            user_id = int(input("what is your user id?\n"))
            password = str(input("what is your password?\n"))

            user_doc = self.userDb.find_one({"_id":user_id})

            if user_doc is None: # type: ignore
                print("No such user exist.")
            else:
                if password == str(user_doc["password"]): # type: ignore
                    print("Login Successfull!!")
                    status = "Logged In"
                    print(f"welcome {str(user_doc["name"])}") # type: ignore
                else:
                    print("incorrect password.")
        
            if login_attempts>=5:
                print("blocked for logging due to 5 unsuccessful attempts")

        return user_doc 

    def logout(self):
        self.driver = None
        return None

if __name__ == "__main__":
    ac = Account("driver")