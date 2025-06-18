from pymongo import MongoClient

class WelcomeScreen:
    def __init__(self):
        self.create_account = 1
        self.login = 2
        self.option = None
        pass

    def welcome_msg(self):
        print("*********Welcome to the uber driver app******")
        print("*********Please chosse your option***********")
        print("1.Create Account \n2.Login ")

        self.option = int(input())
        assert self.option in [1,2], print(f"invalid option selected {self.option}")
        print(f"option selected: {self.option}")
        return None

class Account():
    def __init__(self):
        """
        This is the account class. Handles login and account creation.
        """
        client = MongoClient("mongodb://localhost:27017") # type: ignore
        db = client["uber_clone"] # type: ignore
        self.drivers = db["drivers"] # type: ignore

        w = WelcomeScreen()
        w.welcome_msg()
        if w.option == w.create_account:
            self.create_account()
        elif w.option == w.login:
            self.login()
        else:
            raise Exception("unexpected value of option recieved")
        self.driver = None
    
    def create_account(self):
        """
        This method is used to create account of the driver
        """

        print("We are glad to see you here. It won't take more than a minute to onboard you.")

        #id password
        user_id = int(input("unique user id:\n"))
        password = str(input("set password:\n"))
        confirm_password = str(input("confirm password:\n"))
        while password!= confirm_password:
            print("password did not match.")
            password = str(input("set password:\n"))
            confirm_password = str(input("confirm password:\n"))
        print("password accepted")

        #person info
        name = str(input("what is your name?\n"))
        age = int(input("how old are you?\n"))
        
        #vehicle info
        vehicle_name = str(input("which vehicle do you have?\n"))
        vehicle_number = str(input("what is your vehicle number?\n"))
        x_cord = float(input("your current X coordinate in [1,100]\n"))
        y_cord = float(input("your current Y coordinate in [1,100]\n"))
        
        #financial info
        bank_ac_no = int(input("your current bank account number [10 digit]\n"))
        
        driver_doc = dict({
            "_id": user_id,
            "password": password,
            "name": name,
            "age": age,
            "vehicle_name": vehicle_name,
            "vehicle_number": vehicle_number,
            "x_cord": x_cord,
            "y_cord": y_cord,
            "bank_ac_no": bank_ac_no,
            "balance": 0
        })

        try:
            self.drivers.insert_one(driver_doc) # type: ignore
        except:
            self.drivers.replace_one({"_id": user_id},driver_doc) #type: ignore

        self.driver = driver_doc
        print("account created successfully. You can now login.\n\n\n")
        self.login()

        return None
    
    def login(self):
        print("Welcome to login screen.")
        status = str("attempting login")
        login_attempts = 0
        while status=="attempting login" and (login_attempts<5):
            login_attempts+=1
            try:
                user_id = int(input("what is your user id?\n"))
                password = str(input("what is your password?\n"))

                user_doc = self.drivers.find_one({"_id":user_id})

                if user_doc is None: # type: ignore
                    print("No such user exist.")
                else:
                    if password == str(user_doc["password"]): # type: ignore
                        print("Login Successfull!!")
                        status = "Logged In"
                        print(f"welcome {str(user_doc["name"])}") # type: ignore
                    else:
                        print("incorrect password.")
            except:
                pass

            if login_attempts>=5:
                print("blocked for logging due to 5 unsuccessful attempts")

        return user_doc 

    def logout(self):
        self.driver = None
        return None

class finances:
    def check_balance(self):
        raise NotImplementedError

    def accept_payment(self):
        raise NotImplementedError
    
class user_requests:
    def fetch_requests(self):
        raise NotImplementedError

    def accept_requests(self):
        raise NotImplementedError
    
    def reject_requests(self):
        raise NotImplementedError

class ride:
    def start_ride(self):
        raise NotImplementedError
    def end_ride(self):
        raise NotImplementedError
    

if __name__ == "__main__":
    ac = Account()
