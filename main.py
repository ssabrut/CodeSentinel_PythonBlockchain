from blockchain import Blockchain

network = Blockchain()

# Adding data
network.add_block("User 1 Registered")
network.add_block("User 2 Registered")
network.add_block("User 3 Registered")

# Adding transaction data
network.add_block("From: User 1, To: User 2, Amount: $200")
network.add_block("From: User 2, To: User 3, Amount: $20")

print(network)