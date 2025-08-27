from blockchain import Blockchain
from wallet import generate_wallet


def verify_chain_integrity(network: Blockchain) -> None:
    for i in range(1, len(network.chain)):
        current_block = network.chain[i]
        previous_block = network.chain[i - 1]

        if current_block.previous_hash != previous_block.hash:
            print(f"Chain is broken at Block {current_block.index}!")
            print(f"Expected Previous Hash: {previous_block.hash}")
            print(f"Got Previous Hash:      {current_block.previous_hash}")
            break
        else:
            print(
                f"Block {current_block.index} is linked correctly to Block {previous_block.index}."
            )


if __name__ == "__main__":
    network = Blockchain()

    peepee = generate_wallet()
    peepo = generate_wallet()
    poopoo = generate_wallet()

    # Adding transaction data
    network.add_block(
        {
            "from": peepee["wallet_address"],
            "to": peepo["wallet_address"],
            "amount": "0.0017 BTC",
        }
    )

    network.add_block(
        {
            "from": peepo["wallet_address"],
            "to": poopoo["wallet_address"],
            "amount": "0.000017 BTC",
        }
    )

    network.add_block(
        {
            "from": peepee["wallet_address"],
            "to": poopoo["wallet_address"],
            "amount": "0.000517 BTC",
        }
    )

    # Verify chain integrity
    verify_chain_integrity(network=network)

    # Print the full chain
    print("\n===== FULL NETWORK =====")
    print(network, end="\n")

    # Tampering the chain
    network.chain[2].data = {
        "from": peepee["wallet_address"],
        "to": poopoo["wallet_address"],
        "amount": "0.1 BTC",
    }

    network.chain[2].hash = network.chain[2].compute_hash()

    # Verify the chain again
    verify_chain_integrity(network=network)
