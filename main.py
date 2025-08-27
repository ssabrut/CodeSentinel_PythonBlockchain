from blockchain import Blockchain
from wallet import generate_wallet

def verify_chain_integrity(network: Blockchain) -> None:
    for i in range(1, len(network.chain)):
        current_block = network.chain[i]
        previous_block = network.chain[i-1]

        if current_block.previous_hash != previous_block.hash:
            print(f"Chain is broken at Block {current_block.index}!")
            print(f"Expected Previous Hash: {previous_block.hash}")
            print(f"Got Previous Hash:      {current_block.previous_hash}")
            break
        else:
            print(f"Block {current_block.index} is linked correctly to Block {previous_block.index}.")

if __name__ == "__main__":
    network = Blockchain()

    # Adding data
    network.add_block("User 1 Registered")
    network.add_block("User 2 Registered")
    network.add_block("User 3 Registered")

    # Adding transaction data
    network.add_block("From: User 1, To: User 2, Amount: $200")
    network.add_block("From: User 2, To: User 3, Amount: $20")

    # Verify chain integrity
    verify_chain_integrity(network=network)

    # Print the full chain
    print("\n===== FULL NETWORK =====")
    print(network, end="\n")

    # Tampering the chain
    network.chain[2].data = "From: User 3, To: User 1, Amount: $2000"
    network.chain[2].hash = network.chain[2].compute_hash()

    # Verify the chain again
    verify_chain_integrity(network=network)