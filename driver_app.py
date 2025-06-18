from account_handling import Account
from utils import TypeHandling 
import yaml

DRIVER_QXNS_PATH = "user_info/drivers_qxns.yaml"

class DriverAccount(Account):
    def __init__(self):
        super().__init__("driver")
        
    def _info_seeker(self):
        with open(DRIVER_QXNS_PATH, "r") as f:
            data = yaml.safe_load(f)
        doc = dict()
        for qxn in data['questions']:
            doc[qxn['key']] = input(qxn['text'])
            th = TypeHandling()
            doc = th.type_fixer(qxn, doc)
        return doc 
    

class finances:
    def check_balance(self):
        raise NotImplementedError

    def accept_payment(self):
        raise NotImplementedError
    
class UserRequests:
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
    ac = DriverAccount()
