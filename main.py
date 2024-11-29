from user.server import Server
from user.network import Network
from user.customer import Customer

from blockchain.blockchain import Blockchain

# Blockchain
blockchain = Blockchain(3)

# servers
s1 = Server("alice", blockchain)
s2 = Server("bob", blockchain)

c1 = Customer("jake")
c2 = Customer("alien")

# Netowkr
network = Network(servers = [s1, s2], users = [c1, c2], blockchain = blockchain)

network.add_transaction(c1.add_bitcoins(20))
network.add_transaction(c1.add_bitcoins(40))
network.add_transaction(c1.send_bitcoins(c2, 21)) 
network.add_transaction(c1.add_bitcoins(60))

for i in [c1, c2, s1, s2]:
    print(i.get_balance())

blockchain.b() 


