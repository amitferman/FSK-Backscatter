import numpy as np
import hamming
import crc8
import utils
import math

preamble = "10101010"
packet_len = 4 * 4 # 20 data bits per packet, must be multiple of four

# Returns packet (string of bits) with the following structure:
#   10101010...Hamming(data_bits)...Hamming(CRC-8(data_bits)))
def encode_packet(data_bits):
    # Compute CRC-8 (HD = 6).
    hash = crc8.crc8()
    hash.update(data_bits.encode(encoding="utf-8"))
    crc_bytes = hash.digest()
    crc = ''.join(format(byte, '08b') for byte in crc_bytes)

    # Pad both data bits and crc.
    data_padded = hamming.encode_hamming(data_bits + crc)
    

    return preamble + data_padded

# Returns list of packets.
def encode_packet_stream(bits):
    packets = []
    for i in range(math.ceil(len(bits) / packet_len)):
        packets.append(encode_packet(bits[i * packet_len: (i + 1) * packet_len]))
    return packets

# Decodes packet (string of bits) with the following structure:
#   10101010...Hamming(data_bits)...Hamming(CRC-8(data_bits)))
def decode_packet(bits):
    preamble_len = len(preamble)
    padded_payload = bits[preamble_len:]

    # Attempt error correction according to Hamming codes.
    payload = hamming.decode_hamming(padded_payload)
    data = payload[:-8]
    found_crc = payload[-8:]

    # Check CRC-8.
    hash = crc8.crc8()
    hash.update(data.encode(encoding="utf-8"))
    actual_crc_bytes = hash.digest()
    actual_crc = ''.join(format(byte, '08b') for byte in actual_crc_bytes)

    if (found_crc != actual_crc):
        raise Exception("CRC misamtch.")

    return data

# Decodes packet stream with fuzzy preamble matching
def decode_packet_stream(bits):
    preamble_len = len(preamble)
    packet_content_len = (packet_len // 4 + 2) * 7

    decoded_packets = []
    start_index = 0

    while start_index < len(bits):
        packet_start = fuzzy_match_preamble(bits, preamble, start_index, max_errors=1)
        
        try:
            if packet_start == -1:
                break

            packet_end = packet_start + preamble_len + packet_content_len
            packet_bits = bits[packet_start:packet_end]
            decoded_packet = decode_packet(packet_bits)
            decoded_packets.append(decoded_packet)

            start_index = packet_end
        except Exception:
            start_index += 1

    return decoded_packets

# Performs fuzzy substring matching; matches occur when Hamming Distance is <= max_errors.
def fuzzy_match_preamble(stream, preamble, start_index, max_errors=1):
    preamble_length = len(preamble)
    for i in range(start_index, len(stream) - preamble_length + 1):
        window = stream[i:i+preamble_length]
        distance = hamming_distance(window, preamble)
        if distance <= max_errors:
            print("Matched on index %d" % (i))
            return i

# Computes Hamming Distance between two strings of bits.
def hamming_distance(s1, s2):
    return sum(bit1 != bit2 for bit1, bit2 in zip(s1, s2))

# Fuzz testing on random payloads. Tests 1 bit flip.
if __name__ == "__main__":
    import random
    import utils

    test_len = 16
    for i in range(5):
        print("Test #%d" % (i + 1))
        plaintext = ''.join(random.choice('01') for _ in range(test_len))
        print("\tPlaintext =\t%s" % (plaintext))
        encoded = ''.join(encode_packet_stream(plaintext))
        print("\tEncoded =\t%s" % (encoded))
        flipped = utils.flip_bit(encoded, random.randint(0, test_len - 1))
        print("\tFlipped =\t%s" % (flipped))
        decoded = ''.join(decode_packet_stream(flipped))
        print("\tDecoded =\t%s" % (decoded))
        print("Success" if plaintext == decoded else "Failure")
