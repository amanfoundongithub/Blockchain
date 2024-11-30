from user.server import Server
from user.network import Network
from user.customer import Customer

from blockchain.blockchain import Blockchain

from const import BITCOIN, ETHERNUM


# Blockchain
blockchain = Blockchain()

# servers
s1 = Server("alice", blockchain)
s2 = Server("bob", blockchain)

c1 = Customer("jake")
c2 = Customer("alien")


# Network 
network = Network(servers = [s1, s2], users = [c1, c2], blockchain = blockchain, currency = ETHERNUM)

c3 = Customer("lake")
c4 = Customer("hannah")


network.add_user_to_network(c3)
network.add_user_to_network(c4) 

network.add_transaction(c1.add(20))
network.add_transaction(c1.add(40))
network.add_transaction(c1.send(c2, 21)) 
network.add_transaction(c1.add(60))
network.add_transaction(c2.send(c3, 25))
network.add_transaction(c3.send(c2, 5))
network.add_transaction(c4.add(200))


network.get_user_details()


blockchain.b() 


