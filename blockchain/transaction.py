

class Transaction(object):
    """ 
    Defines the transaction of Bitcoins 
    """
    def __init__(self, 
                 sender : str, 
                 reciever : str,
                 amount : int):
        
        self.reciever = reciever
        self.sender   = sender 
        
        self.amount = amount 
    
    def __repr__(self) -> str:
        return f"[{self.sender} -> {self.reciever}, Amount : {self.amount}]"

