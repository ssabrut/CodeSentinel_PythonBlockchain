import hashlib
import time
from typing import Any


class Block:
    def __init__(self, index: int, data: Any, previous_hash: Any) -> None:
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_string = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
        )
        encoded_block_string = block_string.encode()
        sha256 = hashlib.sha256()
        sha256.update(encoded_block_string)
        return sha256.hexdigest()

    def __repr__(self) -> str:
        return f"""Block(Index: {self.index}, Timestamp: {self.timestamp}, Data: {self.data}, Hash: {self.hash}. Previous Hash: {self.previous_hash})"""


if __name__ == "__main__":
    genesis_block = Block(
        index=0,
        data="Genesis Block",
        previous_hash="0000000000000000000000000000000000000000000000000000000000000000",
    )
    print(genesis_block)
