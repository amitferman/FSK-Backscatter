# University of Washington
# CSE 493W: Wireless Communication, Spring 2023
# Author: Amit Ferman
# 
# Tests channel packetization/decoding. More extensive than those in channel.py.

import sys
sys.path.append("channel_coding")
import channel
import bit_utils
import numpy as np
np.set_printoptions(precision = 2)



def main():
    file_payload = "./channel_coding/payloads/payload_test.txt"
    file_packets = "./channel_coding/packets/packets_test.txt"

    # Read plaintext payload from disk.
    with open(file_payload, "r") as file:
        data_str = file.read()

    # TEST 1: No bit flips.

    # Convert to bits per ASCII.
    data_bits = bit_utils.string_to_bits(data_str)

    # Construct packet stream, each with structure:
    #   10101010...Hamming(data_bits)...Hamming(CRC-8(data_bits)))
    packets = channel.encode_packet_stream(data_bits)

    # Concatenate packet bits.
    packet_bits = ''.join(packets)

    # Save packet bits to file for debugging
    with open(file_packets, 'w') as file:
            file.write(packet_bits)

    # Decode packet bits to original data_bits.
    decoded_data_bits = ''.join(channel.decode_packet_stream(packet_bits))

    # Decode bits to characters
    decoded_data_str = bit_utils.bits_to_string(decoded_data_bits)
    
    # Info.
    print("Test #1")
    print("\tPlaintext =\t%s" % (data_str))
    print("\tDecoded Plaintext =\t\t%s" % (decoded_data_str))
    print("Success" if data_str == decoded_data_str else "Failure")

    # TODO: Test bit flips and error correction.

if __name__ == '__main__':
    main()
