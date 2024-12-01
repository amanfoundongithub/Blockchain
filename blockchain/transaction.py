from const import CREDIT, DEBIT
import time 

class Transaction(object):
    """ 
    Defines the transaction of CryptoCurrency 
    
    Args
    ---
    *Sender* : The ID of the Sender who is sending the money 
    
    *Reciever* : The ID of the Reciever who is recieving the money
    
    *Amount* : Amount to be sent 
    
    ---
    For increasing your own wallet, you can set Sender = Reciever on the Transaction 
    """
    def __init__(self, 
                 sender : str, 
                 reciever : str,
                 amount : int):
        
        self.reciever = reciever
        self.sender   = sender 
        
        self.amount = amount 
        
        self.timestamp = time.time()
    
    def get_transaction_type(self):
        """ 
        Get transaction type
        """
        if self.sender == self.reciever:
            return CREDIT
        else: 
            return DEBIT 
        
    
    def __repr__(self) -> str:
        return f"[{self.sender} -> {self.reciever}, Amount : {self.amount}, {self.timestamp}]"

