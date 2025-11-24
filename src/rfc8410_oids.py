#!/usr/bin/env python3
"""
Script to create and print DER-encoded AlgorithmIdentifier structures
for Ed25519 and Ed448 algorithms.
"""
from typing import List

from pyasn1.codec.der.encoder import encode
from pyasn1.type import univ
from pyasn1_alt_modules import rfc8410, rfc5280


def get_algid_der_hex(oid: univ.ObjectIdentifier) -> str:
    """
    Creates an AlgorithmIdentifier for the given OID and returns its
    DER encoding as a hex string.

    Args:
        oid: The Object Identifier for the algorithm.

    Returns:
        Hexadecimal string of the DER encoded AlgorithmIdentifier.
    """
    algid = rfc5280.AlgorithmIdentifier()
    algid['algorithm'] = oid
    # Parameters are absent for Ed25519 and Ed448 (RFC 8410)

    encoded = encode(algid)
    return encoded.hex()


def print_algid_info(oid: univ.ObjectIdentifier) -> None:
    """
    Prints the pretty representation and DER hex string of the
    AlgorithmIdentifier for the given OID.
    """
    # Create a temporary object just for pretty printing to match original behavior
    algid = rfc5280.AlgorithmIdentifier()
    algid['algorithm'] = oid

    print(algid.prettyPrint())

    hex_str = get_algid_der_hex(oid)
    print(hex_str)
    print('=' * 50)


def main() -> None:
    """
    Main execution function.
    """
    # List of OIDs to process
    oids: List[univ.ObjectIdentifier] = [
        rfc8410.id_Ed25519,
        rfc8410.id_Ed448,
    ]

    for oid in oids:
        print_algid_info(oid)


if __name__ == '__main__':
    main()
