import math


def railfence(plaintext, key):
    ciphertext = ""
    for i in range(key):
        for j in range(i, len(plaintext), key):
            ciphertext += plaintext[j]
    return ciphertext


def railfence_decrypt(cipherText, key):
    plaintext_decrypted = ""
    rail = [['\n' for i in range(math.ceil(len(cipherText) / key))] for j in range(key)]
    for i in range(len(rail)):
        for j in range(len(rail[0])):
            try:
                rail[i][j] = cipherText[i * len(rail[0]) + j]
            except IndexError:
                pass

    for i in range(len(rail[0])):
        for j in range(len(rail)):
            if rail[j][i] != '\n':
                plaintext_decrypted += rail[j][i]

    print(rail)
    return plaintext_decrypted


if __name__ == '__main__':
    plaintext = input("Enter the plaintext: ")
    key = int(input("Enter the key: "))
    ciphertext = railfence(plaintext, key)
    print(ciphertext)
    decrypted = railfence_decrypt(ciphertext, key)
    print(decrypted)