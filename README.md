# CodeSentinel_PythonBlockchain

This will generate wallets, add transactions to the blockchain, verify chain integrity, and demonstrate tampering detection.

This project demonstrates how to build a basic blockchain in Python.

## Requirements

- **Block Structure**: Each block should have:
  - `index`
  - `timestamp`
  - `data`
  - `previous hash`
  - `hash`
- **Hashing Mechanism**: Use SHA-256 to hash block contents.
- **Add Blocks**: A function to add new blocks to the chain.
- **Testing**: Add sample data and print the full blockchain

[//]: # (How to Run the Code)

## Prerequisites

- Python 3.10 or higher
- Install required Python packages:
  - cryptography

You can install the required package using pip:

```bash
pip install cryptography
```

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the main script:

```bash
python main.py
```
