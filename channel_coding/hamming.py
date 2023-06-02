# University of Washington
# CSE 493W: Wireless Communication, Spring 2023
# Author: Amit Ferman
# 
# Implements Hamming(7, 4) codes for error correction.

import bit_utils

# Pads every four data bits with three ceck bits using Hamming(7, 4).
# Input must be a string of 1s and 0s whose length is a multiple of four.
# Noteably, check bits are AFTER data bits according to this implementation.
def encode_hamming(bits):
    if (len(bits) % 4 != 0):
        raise Exception("Plaintext length must be multiple of 4.")

    res = ""
    for i in range(0, len(bits), 4):
        data_bits = bits[i:i+4]
        check_bits = calculate_check_bits(data_bits)
        res += data_bits + check_bits

    return res

# Decodes an encoded string of data bits and check bits using Hamming(7, 4).
# Input must be a string of 1s and 0s whose length is a multiple of four.
# Each three code bits must be positioned immediately after their respective
# four data bits.
def decode_hamming(bits):
    if (len(bits) % 7 != 0):
        raise Exception("Encoded length must be multiple of 7.")

    res = ""
    num_corrections = 0
    for i in range(0, len(bits), 7):
        group = bits[i:i+7]
        data_bits = group[:4]
        parity_bits = group[4:]
    
        syndrome = calculate_syndrome(data_bits, parity_bits)
        error_index = find_error_bit_index(syndrome)

        
        if error_index is not None:
            corrected_group = bit_utils.flip_bit(group, error_index)
            res += corrected_group[:4]
            num_corrections += 1
        else:
            res += data_bits

    print("Decoded with %d corrections." % (num_corrections))
    return res

# Computes check bits for given data bits as string of length three.
def calculate_check_bits(data_bits):
    syndrome = calculate_syndrome(data_bits, '000')
    return (bin(syndrome)[2:]).zfill(3)

# Computes syndrome for given data and parity bits.
def calculate_syndrome(data_bits, parity_bits):
    syndrome = 0
    for i in range(3):
        check_bit_position = 2 - i
        parity_bit = int(parity_bits[i])
        syndrome += (parity_bit ^ compute_parity(data_bits, check_bit_position)) << check_bit_position
    return syndrome

# Computes parity bit (0-indexed) for the given data bits.
def compute_parity(data_bits, check_bit_position):
    # Hamming(7, 4) mapping from data bits to indices used by check bits
    # _e_ _e_ 011 _e  101 110 111
    # 001 010 011 100 101 110 111
    parity = 0
    ecb = 1 << check_bit_position
    if (3 & ecb):
        parity ^= int(data_bits[0])
    if (5 & ecb):
        parity ^= int(data_bits[1])
    if (6 & ecb):
        parity ^= int(data_bits[2])
    if (7 & ecb):
        parity ^= int(data_bits[3])
    return parity

# Maps syndrome to bit index in the layout:
#   [Check Bit 0, Check Bit 1, Check Bit 2, Data Bit 0, Data Bit 1, Data Bit 2, Data Bit 3]
def find_error_bit_index(error_index):
    syndrome_map = {
        1: 4, # check bit 1
        2: 5, # check bit 2
        4: 6, # check bit 3
        3: 0, # data bit 1
        5: 1, # data bit 1
        6: 2, # data bit 1
        7: 3, # data bit 1
    }
    
    return syndrome_map[error_index] if error_index > 0 else None

# Fuzz testing.
if __name__ == "__main__":
    import random

    for i in range(5):
        print("Test #%d" % (i + 1))
        plaintext = ''.join(random.choice('01') for _ in range(16))
        print("\tPlaintext =\t%s" % (plaintext))
        encoded = encode_hamming(plaintext)
        print("\tEncoded =\t%s" % (encoded))
        flipped = bit_utils.flip_bit(encoded, random.randint(0, 15))
        print("\tFlipped =\t%s" % (flipped))
        decoded = decode_hamming(flipped)
        print("\tDecoded =\t%s" % (decoded))
        print("Success" if plaintext == decoded else "Failure")
