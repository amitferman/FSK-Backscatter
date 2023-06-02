# University of Washington
# CSE 493W: Wireless Communication, Spring 2023
# Author: Amit Ferman
# 
# Defines packetization and packet decoding. Each packet with
# payload data_bits has the following structure:
#   10101010...Hamming(data_bits)...Hamming(CRC-8(data_bits)))
# Hamming codes have 4 data bits, 3 check bits; no extra parity
# bit is included to provide error detection in addition to
# 1-bit error correction.

import hamming
import crc
import bit_utils
import math

preamble = "10101010"
packet_nibbles = 4

preamble_len = len(preamble)
packet_len = packet_nibbles * 4 # packet length must be multiple of 4

# Returns length of packet (including preamble and contents)
def get_packet_len():
    return (packet_nibbles + 2) * 7 + preamble_len

# Returns packet from given data bits.
#   data_bits - string of 1s and 0s to encode in packet payload.
#
# Returns string of 1s and 0s representing packet data.
def encode_packet(data_bits):
    # Compute CRC-8
    crc_8 = crc.compute_crc_8(data_bits)

    # Pad both data bits and crc with Hamming check bits.
    data_padded = hamming.encode_hamming(data_bits + crc_8)
    
    return preamble + data_padded

# Partitions given data into list of packets.
#   bits - string of 1s and 0s to encode into packets
#
# Returns list of packets, each of which is a string of
# 1s and 0s representing packet data.
def encode_packet_stream(bits):
    packets = []
    for i in range(math.ceil(len(bits) / packet_len)):
        packets.append(encode_packet(bits[i * packet_len: (i + 1) * packet_len]))
    return packets

# Decodes packet from given packet bits.
#   bits - packet bits to decode as string of 1s and 0s
#
# Returns decoded (and potentially error-corrected) packet
# payload, or raises an exception if the packet is invalid.
def decode_packet(bits):
    padded_payload = bits[preamble_len:]

    # Attempt error correction according to Hamming codes.
    payload = hamming.decode_hamming(padded_payload)

    # Check CRC-8.
    data = payload[:-8]
    found_crc = payload[-8:]
    actual_crc = crc.compute_crc_8(data)

    if (found_crc != actual_crc):
        raise Exception("CRC misamtch.")

    return data

# Decodes packet stream with fuzzy preamble matching.
#   bits - bit stream of 1s and 0s representing packet stream.
#
# Returns list of packets that could be successfully parsed from the stream.
def decode_packet_stream(bits):
    packet_content_len = get_packet_len() - preamble_len
    decoded_packets = []
    

    # For each fuzzy preamble match,
    #  if packet cannot be decoded, then skip to next start index
    #  otherwise, skip by packet length
    start_index = 0
    while start_index < len(bits):
        packet_start = fuzzy_match_preamble(bits, start_index, max_errors=1)

        # Break if no more matches.
        if packet_start == -1:
                break

        # Attempt to decode packet from matched preamble.
        try:
            packet_end = packet_start + preamble_len + packet_content_len
            packet_bits = bits[packet_start:packet_end]
            decoded_packet = decode_packet(packet_bits)
            decoded_packets.append(decoded_packet)
            start_index = packet_end
        except Exception:
            start_index += 1

    return decoded_packets

# Performs fuzzy substring matching from start_index; matches
# occur when Hamming Distance is <= max_errors.
#   bits        - bit stream in which to find the next preamble match
#                   as string of 1s and 0s
#   start_index - first index (inclusive) from which this method
#                   looks for matches
#   max_errors  - max hamming distance per match.
#
# Returns index into bits of first matched bit, or -1 if none found.
def fuzzy_match_preamble(bits,start_index, max_errors=1):
    for i in range(start_index, len(bits) - preamble_len + 1):
        window = bits[i:i+preamble_len]
        distance = hamming_distance(window, preamble)
        if distance <= max_errors:
            return i

# Computes Hamming Distance between two strings of bits.
#   s1 - first string of 1s and 0s
#   s2 - second string of 1s and 0s
#
# Returns hamming distance
def hamming_distance(s1, s2):
    return sum(bit1 != bit2 for bit1, bit2 in zip(s1, s2))

# Fuzz testing on random payloads. Tests 1 bit flip.
if __name__ == "__main__":
    import random

    test_len = 16
    for i in range(5):
        print("Test #%d" % (i + 1))
        plaintext = ''.join(random.choice('01') for _ in range(test_len))
        print("\tPlaintext =\t%s" % (plaintext))
        encoded = ''.join(encode_packet_stream(plaintext))
        print("\tEncoded =\t%s" % (encoded))
        flipped = bit_utils.flip_bit(encoded, random.randint(0, test_len - 1))
        print("\tFlipped =\t%s" % (flipped))
        decoded = ''.join(decode_packet_stream(flipped))
        print("\tDecoded =\t%s" % (decoded))
        print("Success" if plaintext == decoded else "Failure")
