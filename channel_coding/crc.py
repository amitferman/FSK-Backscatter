# University of Washington
# CSE 493W: Wireless Communication, Spring 2023
# Author: Amit Ferman
# 
# Defines Cyclic Redundancy Check (CRC) API.

import crc8

# Computes CRC-8 from given data bits.
#   data_bits - string of 1s and 0s to hash
#
# Returns string of 1s and 0s representing the CRC.
def compute_crc_8(data_bits):
    hash = crc8.crc8()
    hash.update(data_bits.encode(encoding="utf-8"))
    crc_bytes = hash.digest()
    return ''.join(format(byte, '08b') for byte in crc_bytes)

# Testing.
if __name__ == "__main__":
    print("Test")
    plaintext = "Hello World!12345"
    print("\tPlaintext =\t%s" % (plaintext))
    crc = compute_crc_8(plaintext)
    print("\tCRC-8 =\t\t%s" % (crc))
    print("Success" if crc != None else "Failure")
