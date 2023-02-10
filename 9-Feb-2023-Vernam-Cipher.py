def xor(bit_1, bit_2):
    if bit_1 == bit_2:
        return "0"
    else:
        return "1"


def match_length(first, second):
    if len(first) < len(second):
        for i in range(len(second) - len(first)):
            first = "0" + first
    else:
        for i in range(len(first) - len(second)):
            second = "0" + second
    return first, second


def xor_vernam(char_1, char_2):
    encrypted = ""
    for i in range(len(char_1)):
        encrypted += xor(char_1[i], char_2[i])
    return encrypted


def decrypt(ciphertext, keyword_func, extra_dec):
    decrypt_cipher_ret = ""
    for i in range(len(ciphertext)):
        if ciphertext[i] == " ":
            decrypt_cipher_ret += " "
        else:
            char1 = bin((ord(ciphertext[i]) - 65))
            if extra_dec[i]:
                char1 = bin((ord(ciphertext[i]) - 65) + 26)
            char2 = bin((ord(keyword_func[i]) - 65))
            char1, char2 = char1[2:], char2[2:]
            char1, char2 = match_length(char1, char2)
            temp_cipher = int(xor_vernam(char1, char2), 2)
            if temp_cipher >= 26:
                temp_cipher -= 26
            decrypt_cipher_ret += chr(temp_cipher + 65)
    return decrypt_cipher_ret


def vernam(plaintext_func, keyword_func):
    cipher_ret = ""
    extra = [False for i in range(len(plaintext_func))]
    for i in range(len(plaintext_func)):
        if plaintext_func[i] == " ":
            cipher_ret += " "
        else:
            char1 = bin((ord(plaintext_func[i]) - 65))
            char2 = bin((ord(keyword_func[i]) - 65))
            char1, char2 = char1[2:], char2[2:]
            char1, char2 = match_length(char1, char2)
            temp_cipher = int(xor_vernam(char1, char2), 2)
            if temp_cipher >= 26:
                temp_cipher -= 26
                extra[i] = True
            cipher_ret += chr(temp_cipher + 65)
    return cipher_ret, extra


def key_generation(accepted_plaintext, accepted_key):
    newkey = ""
    if len(accepted_key) < len(accepted_plaintext):
        for i in range(len(accepted_plaintext)):
            newkey += accepted_key[i % len(accepted_key)]
        return newkey
    else:
        return accepted_key


if __name__ == '__main__':
    plaintext = input("Enter the plaintext: ")
    plaintext = plaintext.upper()
    key = input("Enter the key: ")
    key = key.upper()
    keyword = key_generation(plaintext, key)
    print("The Original Text is: {}".format(plaintext.upper()))
    print("The Keyword is: {}".format(keyword.upper()))
    cipher, extra_val = vernam(plaintext, keyword)
    print("The Cipher Text is: {}".format(cipher.upper()))
    decrypt_cipher = decrypt(cipher.upper(), keyword, extra_val)
    print("The Decrypted Text is: {}".format(decrypt_cipher.upper()))
