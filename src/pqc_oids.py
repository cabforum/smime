import binascii

from pyasn1.codec.der.encoder import encode
from pyasn1.type.univ import ObjectIdentifier
from pyasn1_alt_modules import rfc5280


def print_hexstr_algid_for_oid(oid):
	algid = rfc5280.AlgorithmIdentifier()
	algid['algorithm'] = oid

	print(algid.prettyPrint())

	encoded = encode(algid)

	print(binascii.b2a_hex(encoded).decode('us-ascii'))
	print('=' * 50)

print('ML-DSA')
_SIG_ALG_ARC = ObjectIdentifier('2.16.840.1.101.3.4.3')

print_hexstr_algid_for_oid(_SIG_ALG_ARC + (17,))
print_hexstr_algid_for_oid(_SIG_ALG_ARC + (18,))
print_hexstr_algid_for_oid(_SIG_ALG_ARC + (19,))

print('ML-KEM')
_KEM_ARC = ObjectIdentifier('2.16.840.1.101.3.4.4')

print_hexstr_algid_for_oid(_KEM_ARC + (1,))
print_hexstr_algid_for_oid(_KEM_ARC + (2,))
print_hexstr_algid_for_oid(_KEM_ARC + (3,))
