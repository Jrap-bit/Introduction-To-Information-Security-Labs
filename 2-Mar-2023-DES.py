def divide_into_blocks(func_binary):
    block_mat = []
    for i in range(0, len(func_binary), 8):
        block_mat.append(func_binary[i:i + 8])

    if len(block_mat[-1]) < 8:
        for i in range(8 - len(block_mat[-1])):
            block_mat[-1].append('00000000')
    return block_mat


def convert_to_binary(func_plaintext):
    bin_mat = []
    for i in func_plaintext:
        bin_mat.append(format(ord(i), '08b'))
    return bin_mat


if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    binary = convert_to_binary(plaintext)
    print(binary)
    blocks = divide_into_blocks(binary)
    print(blocks)
    print(len(blocks))
