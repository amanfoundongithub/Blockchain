from time import time 
import hashlib

class TransactionBlock(object):
    """ 
    Represents Units that are processed via Blockchain
    
    """
    def __init__(self,
                 prev_hash : str, 
                 list_of_transactions : list,
                 timestamp : float = None):
        
        self.prev_hash = prev_hash
        self.transactions = list_of_transactions
        
        self.timestamp = time() if timestamp is None else timestamp
        
        self.nonce = 0
        
        self.hash = self.__generate_hash() 
    
    def __generate_hash(self):
        repstr = f"{self.prev_hash}{self.transactions}{self.timestamp}{self.nonce}"
        
        return hashlib.sha256(repstr.encode()).hexdigest() 
    
    def mine(self, difficulty : int):
        # We want at least these many 0s initially
        target = "0" * difficulty
        
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.__generate_hash()
        
        
        