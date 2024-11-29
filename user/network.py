import time 
from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction

class Network:
    
    def __init__(self, servers : list, users : list, blockchain : Blockchain):
        
        self.__servers = servers
        self.__blockchain = blockchain
        
        self.__users = {
            user.get_id() : user for user in users + servers 
        }
        
        
    
    def __select_by_proof_of_work(self, transaction):
        # Select the server based on proof of work method
        best_server = None 
        best_transaction = None
        
        
        for i in range(len(self.__servers)):
            # Process here
            transaction = self.__servers[i].solve_pow()
            
            if best_transaction is None or best_transaction.nonce > transaction.nonce:
                best_server = self.__servers[i]
                best_transaction = transaction

        return best_server, best_transaction

    def __verify_proof_of_work(self, transaction):
        
        true = 0
        false = 0
        
        for i in range(len(self.__servers)):
            status = self.__servers[i].verify_pow(transaction)
            
            if status == True: 
                true += 1
            elif status == False:
                false += 1
            else: 
                continue
        
        return true > false 
            
    
    def add_transaction(self, transaction):
        
        self.__blockchain.add_transaction_to_chain(transaction)
        
        best_server, best_transaction = self.__select_by_proof_of_work(transaction)
        
        if self.__verify_proof_of_work(best_transaction) == False: 
            return 
        
        self.__perform_transactions(best_transaction)
        
        # Now add the transactions to the blockchain
        self.__blockchain.add_mined_block_to_chain(best_transaction) 
        self.__blockchain.clear_pending_transactions()
        
        # Now reward the miner
        reward_miner = Transaction(best_server.get_id(),best_server.get_id(), 2)
        self.__blockchain.add_transaction_to_chain(reward_miner)
        
        # Now we end it 
        return 


    def __perform_transactions(self, transactions):
        for i in transactions.transactions:
            if i.sender == i.reciever:
                self.__users[i.sender].add_bitcoin(i.amount) 
            else:
                self.__users[i.sender].reduce_bitcoin(i.amount)
                self.__users[i.reciever].add_bitcoin(i.amount) 
                
            
        
        
        
        