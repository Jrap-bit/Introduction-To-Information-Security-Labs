def vignere(plaintext, keyword_func):
    cipher = ""
    for i in range(len(plaintext)):
        if plaintext[i] == " ":
            cipher += " "
        else:
            char = ((ord(plaintext[i]) - 65) + (ord(keyword_func[i]) - 65))
            cipher += chr((char % 26) + 65)
    return cipher


def vignere_decrypt(ciphertext, keyword_func):
    decrypt_cipher = ""
    for i in range(len(ciphertext)):
        if ciphertext[i] == " ":
            decrypt_cipher += " "
        else:
            char = ((ord(ciphertext[i]) - 65) - (ord(keyword_func[i]) - 65))
            decrypt_cipher += chr((char % 26) + 65)
    return decrypt_cipher


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
    cipher = vignere(plaintext, keyword)
    print("The Cipher Text is: {}".format(cipher.upper()))
    print("The Decrypted Text is: {}".format(vignere_decrypt(cipher, keyword).upper()))
