import time 
import hashlib

class TransactionBlock(object):
    """ 
    Represents Units that are processed via Blockchain
    
    """
    def __init__(self,
                 prev_hash : str, 
                 list_of_transactions : list):
        
        self.prev_hash = prev_hash
        self.transactions = list_of_transactions
        self.timestamp = time.time() 
        
        self.nonce = 0
        
        self.merkle_root = self.__generate_merkle_root()  
        
        self.hash = self.__generate_hash() 
        
        
    
    def __generate_merkle_root(self):
        """
        Generates the Merkle root from the list of transactions.
        """
        # Hash each transaction
        transaction_hashes = [hashlib.sha256(str(tx).encode()).hexdigest() for tx in self.transactions]
        
        # Build the Merkle tree
        while len(transaction_hashes) > 1:
            if len(transaction_hashes) % 2 != 0:  # If odd, duplicate the last hash
                transaction_hashes.append(transaction_hashes[-1])
            
            # Pair up adjacent hashes and hash them
            transaction_hashes = [
                hashlib.sha256((transaction_hashes[i] + transaction_hashes[i + 1]).encode()).hexdigest()
                for i in range(0, len(transaction_hashes), 2)
            ]
        
        # The single remaining hash is the Merkle root
        return transaction_hashes[0] if transaction_hashes else None
    
    def __generate_hash(self):
        repstr = f"{self.prev_hash}{self.transactions}{self.nonce}{self.merkle_root}{self.timestamp}"
        
        return hashlib.sha256(repstr.encode()).hexdigest() 
    
    def mine_pow(self, difficulty : int):
        # We want at least these many 0s initially
        target = "0" * difficulty
        
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.__generate_hash()
        
        
    def mine_pos(self):
        return 
        
        
        
        