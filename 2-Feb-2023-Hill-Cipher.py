import numpy as np


def inverse_matrix(K):
    det = int(np.linalg.det(K))
    det_multiplicative_inverse = pow(det, -1, 26)
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = np.delete(Dji, (j), axis=0)
            Dji = np.delete(Dji, (i), axis=1)
            det = Dji[0][0] * Dji[1][1] - Dji[0][1] * Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1, i + j) * det) % 26
    return K_inv


def multiply_matrix(matrix1, matrix2):
    cipherMatrix = [[0] for i in range(3)]
    print(cipherMatrix)
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (matrix1[i][x] *
                                       matrix2[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
    return cipherMatrix


def decrypt_hill_cipher(ciphertext_func, key):
    key_inv = inverse_matrix(key)
    plaintext = ""
    n = len(ciphertext_func)
    pair = convert_cipher_to_matrix(ciphertext_func, len(key))
    for mat in pair:
        result = np.dot(key_inv, mat)
        plaintext += chr(int(result[0][0] % 26) + ord('A'))
        plaintext += chr(int(result[1][0] % 26) + ord('A'))
        plaintext += chr(int(result[2][0] % 26) + ord('A'))
    return plaintext


def convert_cipher_to_matrix(function_cipher, pair):
    cipher_matrix_func = []
    temp_func = []
    if len(function_cipher) % pair != 0:
        for i in range(pair - len(function_cipher) % pair):
            function_cipher += 'X'
    for i in range(0, len(function_cipher), pair):
        for j in range(pair):
            temp_func.append([ord(function_cipher[i + j]) - 65])
    for i in range(len(function_cipher) // pair):
        cipher_matrix_func.append(temp_func[(pair * i):(pair * i) + pair])
    return cipher_matrix_func


if __name__ == '__main__':
    plaintext = input("Enter the Plain text: ")
    print("The Original Text is: {}".format(plaintext.upper()))
    cipher = plaintext.upper()
    key_matrix = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
    pair_size = len(key_matrix)
    cipher_text_matrix = convert_cipher_to_matrix(cipher, pair_size)
    ciphertext = ""
    for matrix in cipher_text_matrix:
        print(matrix)
        cipher = multiply_matrix(key_matrix, matrix)
        for i in cipher:
            ciphertext += chr(i[0] + 65)
    decrypted_text = decrypt_hill_cipher(ciphertext, key_matrix)
    print("The Ciphertext is: {}".format(ciphertext))
    print("The Decrypted text is: {}".format(decrypted_text))
