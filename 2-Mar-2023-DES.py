def key_gen():
    return '10110010'


def feistel(block_64):
    rounds = 1
    key = key_gen()
    left_block = block_64[:4]
    right_block = block_64[4:]
    for n in range(rounds):
        xor_key_right = []
        new_left = right_block
        new_right = []
        for x in range(len(left_block)):
            xor_key_right.append(xor_8bit(right_block[x], key))
        for i in range(len(left_block)):
            new_right.append(xor_8bit(left_block[i], xor_key_right[i]))
        left_block = new_left
        right_block = new_right
    feistel_ret = left_block + right_block
    return feistel_ret


def xor_8bit(func_a, func_b):
    xor = ''
    for i in range(8):
        if func_a[i] == func_b[i]:
            xor += '0'
        else:
            xor += '1'
    return xor


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


def DES(DES_pt):
    ciphertext = ''
    binary = convert_to_binary(DES_pt)
    # print(binary)
    blocks = divide_into_blocks(binary)
    # print(blocks)
    feisteled = []
    for i in blocks:
        feistel_process = feistel(i)
        feisteled.append(feistel_process)
    print(feisteled)
    return ciphertext


if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    ciphertext = DES(plaintext)
