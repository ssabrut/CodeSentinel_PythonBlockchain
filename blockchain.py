from typing import Any

from block import Block


class Blockchain:
    def __init__(self) -> None:
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        return Block(
            0,
            "Genesis Block",
            "0000000000000000000000000000000000000000000000000000000000000000",
        )

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, data: Any) -> None:
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        previous_hash = latest_block.hash
        new_block = Block(index=new_index, data=data, previous_hash=previous_hash)
        self.chain.append(new_block)

    def __repr__(self) -> str:
        chain = ""
        for block in self.chain:
            chain += str(block) + "\n"
        return chain


if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("Block 1")
    print(blockchain)
