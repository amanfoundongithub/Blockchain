import uuid


class User:
    
    def __init__(self, 
                 name : str):
        
        self._id = str(uuid.uuid4())
        
        self._name = name 
        
        self._balance = 1
        
        self._role = "customer"
    
    def get_name(self):
        return self._name
    
    def get_id(self):
        return self._id

    def get_balance(self):
        return self._balance
    
    def get_role(self):
        return self._role

    def add_bitcoin(self, amt):
        self._balance += amt 
    
    def reduce_bitcoin(self, amt):
        self._balance -= amt 
    