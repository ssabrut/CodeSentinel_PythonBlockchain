from typing import Dict

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat


def generate_wallet() -> Dict[str, str]:
    # Generate private key
    private_key = ec.generate_private_key(ec.SECP256K1())

    # Convert to 64 char hex string
    private_key_hex = hex(private_key.private_numbers().private_value)[2:].zfill(64)

    # Generate public key
    public_key = private_key.public_key()

    # Format the public key
    public_key_hex = public_key.public_bytes(
        encoding=Encoding.X962, format=PublicFormat.UncompressedPoint
    ).hex()

    # Generate wallet address
    # First get the raw public key bytes
    raw_public_key = public_key.public_bytes(
        encoding=Encoding.X962, format=PublicFormat.UncompressedPoint
    )[1:]

    digest = hashes.Hash(hashes.SHA256())
    digest.update(raw_public_key)
    hashed_public_key = digest.finalize()

    # Set the wallet address
    wallet_address = "0x" + hashed_public_key[-20:].hex()
    return {
        "private_key": private_key_hex,
        "public_key": public_key_hex,
        "wallet_address": wallet_address,
    }
