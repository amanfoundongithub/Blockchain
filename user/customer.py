import uuid
from blockchain.blockchain import Blockchain
from blockchain.transactionBlock import TransactionBlock
from blockchain.transaction import Transaction
from user.user import User
from user.network import Network



class Customer(User):
    """
    Customers who are using Bitcoin 
    """
    
    def __init__(self, name):
        super().__init__(name)
    
    def add_bitcoins(self, amount : int):
        # Create a transaction
        transaction = Transaction(self._id, self._id, amount)
        
        return transaction
    
    def send_bitcoins(self, to : User, amount : int):
        transaction = Transaction(self._id, to.get_id(), amount) 
        
        return transaction
    