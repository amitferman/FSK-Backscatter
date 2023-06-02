# University of Washington
# CSE 493W: Wireless Communication, Spring 2023
# Author: Amit Ferman
# 
# Packetizes given file of ASCII characters and saves
# packet bit stream in given destination file.

import argparse
import channel
import bit_utils
import numpy as np
np.set_printoptions(precision = 2)

def main():
    parser = argparse.ArgumentParser(description='Packetizes given payload into a stream of packets, and saves output in the given file.')

    # Parse required payload and packet stream file paths.
    parser.add_argument('--payload', type=str, help='Path to file containing ASCII payload.', default="./channel_coding/payloads/payload.txt", required=False)
    parser.add_argument('--packets', type=str, help='Path to file to store packet bit stream.', default="./channel_coding/packets/packets.txt", required=False)
    args = parser.parse_args()

    # Extracting arguments.
    file_payload = args.payload
    file_packets = args.packets

    # Info.
    print('Payload file:', file_payload)
    print('Packets file:', file_packets)

    # Read plaintext payload from disk.
    with open(file_payload, "r") as file:
        data_str = file.read()

    # Convert to bits per ASCII.
    data_bits = bit_utils.string_to_bits(data_str)

    # Construct packet stream, each with structure:
    #   10101010...Hamming(data_bits)...Hamming(CRC-8(data_bits)))
    packets = channel.encode_packet_stream(data_bits)

    # Concatenate packet bits.
    packet_bits = ''.join(packets)

    # Save packet bits to file.
    with open(file_packets, 'w') as file:
            file.write(','.join(packet_bits))

if __name__ == '__main__':
    main()
