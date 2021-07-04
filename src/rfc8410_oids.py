import binascii

from pyasn1.codec.der.encoder import encode
from pyasn1_alt_modules import rfc8410, rfc5280


def print_hexstr_algid_for_oid(oid):
	algid = rfc5280.AlgorithmIdentifier()
	algid['algorithm'] = oid

	print(algid.prettyPrint())

	encoded = encode(algid)

	print(binascii.b2a_hex(encoded).decode('us-ascii'))
	print('=' * 50)


print_hexstr_algid_for_oid(rfc8410.id_Ed25519)
print_hexstr_algid_for_oid(rfc8410.id_Ed448)
