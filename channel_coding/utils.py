# Converts a string to bits per ASCII encoding. Returns a string of bits.
def string_to_bits(input_string):
    ascii_values = [ord(char) for char in input_string]
    binary_strings = [format(value, '08b') for value in ascii_values]
    bits_string = ''.join(binary_strings)
    return bits_string


# Converts given bits to string per ASCII encoding. Returns a string of characters.
def bits_to_string(bits_string):
    binary_strings = [bits_string[i:i+8] for i in range(0, len(bits_string), 8)]
    decimal_values = [int(binary, 2) for binary in binary_strings]
    output_string = ''.join(chr(value) for value in decimal_values)
    return output_string

# Flips given index in the given bits.
def flip_bit(data_bits, index):
    flipped_bit = '1' if data_bits[index] == '0' else '0'
    return data_bits[:index] + flipped_bit + data_bits[index + 1:]

# Testing.
if __name__ == "__main__":
    print("Test")
    plaintext = "Hello World!12345"
    print("\tPlaintext =\t%s" % (plaintext))
    bits = string_to_bits(plaintext)
    print("\tBits =\t\t%s" % (bits))
    decoded = bits_to_string(bits)
    print("\tDecoded =\t%s" % (decoded))
    print("Success" if plaintext == decoded else "Failure")
