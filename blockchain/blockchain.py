from .transactionBlock import TransactionBlock
from const import GENESIS_BLOCK_HASH, GENESIS_BLOCK_NAME, ETHERNUM, BITCOIN

class Blockchain(object):
    
    def __init__(self,
                 type : str = ETHERNUM,
                 difficulty : int = None):
        
        self.__blockchain = [
            self.init_blockchain() 
        ]
        
        self.difficulty = difficulty
        self.__pending_transaction = [] 
    
    def init_blockchain(self):
        return TransactionBlock(GENESIS_BLOCK_HASH, [GENESIS_BLOCK_NAME]).hash 
    
    def add_transaction_to_chain(self, transaction):
        self.__pending_transaction.append(transaction)
    
    def get_pending_transactions(self):
        return self.__pending_transaction
    
    def clear_pending_transactions(self):
        self.__pending_transaction = []
    
    def get_latest_block_hash(self):
        return self.__blockchain[-1]
    
    def add_mined_block_to_chain(self, block):
        self.__blockchain.append(block.hash) 
        
    
    def b(self):
        for i in self.__blockchain:
            # print(i.hash, i.timestamp, i.transactions, i.nonce)
            print(i)
        
        
        
        
        
       