from account_handling import Account
from utils import TypeHandling
import yaml

CUSTOMER_QXNS_PATH = "user_info/customers_qxns.yaml"

class CustomerAccount(Account):
    def __init__(self):
        super().__init__("customer")
        
    def _info_seeker(self):
        with open(CUSTOMER_QXNS_PATH, "r") as f:
            data = yaml.safe_load(f)
        doc = dict()
        for qxn in data['questions']:
            doc[qxn['key']] = input(qxn['text'])
            th = TypeHandling()
            doc = th.type_fixer(qxn, doc)
        return doc 


if __name__ == "__main__":
    c = CustomerAccount()