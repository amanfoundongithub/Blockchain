import uuid
from blockchain.blockchain import Blockchain
from blockchain.transactionBlock import TransactionBlock
from blockchain.transaction import Transaction
from user.user import User


class Server(User):
    """ 
    BitCoin Miners
    """
    def __init__(self,
                 name : str, 
                 blockchain : Blockchain):
        super().__init__(name) 
        
        # Blockchain managed by the Node
        self.__blockchain = blockchain
        
        self._role = "server"
    
    
    def solve_pow(self):
        try:
            # Get the pending transactions
            pending_transactions = self.__blockchain.get_pending_transactions()
            
            if len(pending_transactions) == 0:
                raise ValueError("Empty transaction provided")
        
            # Get the latest hash
            prev_hash = self.__blockchain.get_latest_block_hash()
        
            # Now create a transaction block
            transaction = TransactionBlock(prev_hash, pending_transactions)
            
            # Mine this transaction  
            transaction.mine_pow(self.__blockchain.difficulty)
            
            return transaction
        
        except Exception as e:
            print(e)
            return None
    
    def verify_pow(self, transaction : TransactionBlock):
        try: 
            if transaction.hash.startswith("0" * self.__blockchain.difficulty) == False:
                return False 
            return True
        except Exception as e:
            print(e)
            return None 
    
    
    def solve_pos(self):
        try:
            # Get the pending transactions
            pending_transactions = self.__blockchain.get_pending_transactions()
            
            if len(pending_transactions) == 0:
                raise ValueError("Empty transaction provided")
        
            # Get the latest hash
            prev_hash = self.__blockchain.get_latest_block_hash()
        
            # Now create a transaction block
            transaction = TransactionBlock(prev_hash, pending_transactions)
            
            # Mine this transaction  
            transaction.mine_pos()
            
            return transaction
        
        except Exception as e:
            print(e)
            return None
        
    def verify_pos(self, transaction : TransactionBlock):
        try: 
            return True
        except Exception as e:
            print(e)
            return None   