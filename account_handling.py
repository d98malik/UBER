from pymongo import MongoClient
import yaml
import json 

class Account:
    def __init__(self,type:str):
        """
        This is the account class. Handles login and account creation.
        """
        assert type in ["drivers","passengers"], print("invalid type")

        client = MongoClient("mongodb://localhost:27017") # type: ignore
        self.db = client["uber_clone"] # type: ignore

        if type == "drivers": 
            self.userDb = self.db["drivers"]
        else:
            self.userDb = self.db["passengers"]

        self.user_doc = None


    def create_account(self, info: json):
        """
        This method is used to create account for the user.
        """
        try:
            self.userDb.insert_one(info) 
        except:
            self.userDb.replace_one({"_id":info["_id"]},info)    
        self.user_doc = info 
        print("account created successfully. You can now login.\n\n\n")
        
        return "Account created successfully."
    

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