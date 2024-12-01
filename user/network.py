import time 
from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction

from const import CREDIT, DEBIT
from const import BITCOIN, ETHERNUM

import random 

from tabulate import tabulate

class Network:
    
    def __init__(self, servers : list, users : list, blockchain : Blockchain):
        
        self.__servers = servers
        self.__blockchain = blockchain
        
        self.__users = {
            user.get_id() : user for user in users + servers 
        }
        
        self.currency = blockchain.currency
        
        self.symbol = "BTC" if blockchain.currency == BITCOIN else "ETH"
        
    
    def add_server_to_network(self, server):
        self.__users[server.get_id()] = server 
        self.__servers.append(server) 
        print(f"Added server {server.get_name()} to the network!")
    
    def add_user_to_network(self, user):
        self.__users[user.get_id()] = user    
        print(f"Added user {user.get_name()} to the network!")
    
    def remove_user_from_network(self, user):
        self.__users.pop(user.get_id())
    
    def get_user_details(self):
        table = [
            ["Name", f"Balance ({self.symbol})", "Role In Network"]
        ]
        
        for key in self.__users: 
            user = self.__users[key]
            
            table.append(
                [user.get_name(),user.get_balance(), user.get_role()]
            )
        
        table.sort(key = lambda x : x[-1])
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    
    
    def add_transaction(self, transaction):
        
        self.__blockchain.add_transaction_to_chain(transaction)
        if len(self.__blockchain.get_pending_transactions()) < 5:
            return 
        
        if self.currency == BITCOIN:
            # Verify the transaction by using Merkle tree
            best_server, best_transaction = self.__verify_bitcoin_transaction() 
            
            # If verification failed 
            if best_server is None: 
                return 
            
            # Now we perform the transaction adding and removing
            self.__perform_transactions(best_transaction)
            
            # Now we add this block to the blockchain
            self.__blockchain.add_mined_block_to_chain(best_transaction)
            self.__blockchain.clear_pending_transactions() 
            
            # Now we reward the miner for their effort (2 BTC)
            reward_miner = Transaction(best_server.get_id(), best_server.get_id(), 2)
            self.__blockchain.add_transaction_to_chain(reward_miner)
            
            return 
        
        elif self.currency == ETHERNUM:
            # Verify the transaction by using Merkle tree
            best_server, best_transaction = self.__verify_ethereum_transaction() 
            
            # If verification failed 
            if best_server is None: 
                return 
            
            # Now we perform the transaction adding and removing
            self.__perform_transactions(best_transaction)
            
            # Now we add this block to the blockchain
            self.__blockchain.add_mined_block_to_chain(best_transaction)
            self.__blockchain.clear_pending_transactions() 
            
            # Now we reward the miner for their effort (2 BTC)
            reward_miner = Transaction(best_server.get_id(), best_server.get_id(), 2)
            self.__blockchain.add_transaction_to_chain(reward_miner)
            
            return
        else:
            pass 


    def __perform_transactions(self, transactions):
        for i in transactions.transactions:
            typ = i.get_transaction_type()
            if typ == CREDIT:
                self.__users[i.sender].add_bitcoin(i.amount) 
            else:
                self.__users[i.sender].reduce_bitcoin(i.amount)
                self.__users[i.reciever].add_bitcoin(i.amount) 
    
    def __verify_bitcoin_transaction(self):
        # Compute Merkel tree
        original_transaction = self.__servers[0].solve_pow()
        
        # Store the nonce 
        best_server = self.__servers[0]
        best_transaction = original_transaction
        
        # Merkel root
        merkle_root_original = original_transaction.merkle_root
        
        valid = 0.0
        invalid = 0.0
        
        for i in range(1, len(self.__servers)):
            # For each node, get the transaction
            new_transaction = self.__servers[i].solve_pow()
            
            if new_transaction.merkle_root != merkle_root_original:
                print(f"Invalid transaction detected by server #{i + 1}, named {self.__servers[i].get_name()}")
                invalid += 1
            else: 
                print(f"Signature verified by #{i + 1}") 
                valid += 1
            
            if new_transaction.nonce < best_transaction.nonce:
                best_server = self.__servers[i]
                best_transaction = new_transaction
        
        if valid < 2*invalid: 
            # Byzantine Fault Tolerance
            print("Invalid Transaction Block, Operation Aborted")
            return None, None 
        
        return best_server, best_transaction 
    
    def __verify_ethereum_transaction(self):
        # Use monetary weight to select a new server 
        wallets = [self.__servers[i].get_balance() for i in range(len(self.__servers))]
        server  = random.choices(self.__servers, weights = wallets, k = 1)[0]
        
        # Compute Merkel tree
        original_transaction = server.solve_pos()
        
        # Merkel root
        merkle_root_original = original_transaction.merkle_root
        
        valid = 0.0
        invalid = 0.0
        
        for i in range(1, len(self.__servers)):
            # For each node, get the transaction
            new_transaction = self.__servers[i].solve_pos()
            
            if new_transaction.merkle_root != merkle_root_original:
                print(f"Invalid transaction detected by server #{i + 1}, named {self.__servers[i].get_name()}")
                invalid += 1
            else: 
                print(f"Signature verified by #{i + 1}") 
                valid += 1
        
        if valid < 2*invalid: 
            # Byzantine Fault Tolerance
            print("Invalid Transaction Block, Operation Aborted")
            return None, None 
        
        return server, original_transaction    