import PrimeGen as pg


def calc_d(e, phi):
    t1 = 0
    t2 = 1
    r1 = phi
    r2 = e
    while r2 > 0:
        q = r1 // r2
        r = r1 % r2
        r1 = r2
        r2 = r
        t = t1 - q * t2
        t1 = t2
        t2 = t
        if r1 == 1:
            return t1 % phi


def keygen():
    n = int(input("Enter the number of bits: "))
    p = pg.main(n)
    while True:
        q = pg.main(n)
        if q != p:
            break
    n = p * q
    phi = (p - 1) * (q - 1)
    e = int(input("Enter the value of e: ") or "65537")
    d = calc_d(e, phi)

    print("p: {}\n\nq: {}".format(p, q))
    print()
    print("n: {}".format(n))
    print()
    print("phi: {}".format(phi))
    print()
    print("e: {}".format(e))
    print()
    print("d: {}".format(d))
    print()
    print("Public Key: ({}, {})".format(e, n))
    print()
    print("Private Key: ({}, {})".format(d, n))
    print()

    return e, d, n


def RSA(plaintext, e, d, n):
    ciphertext = []
    for i in plaintext:
        char = ord(i) - 65
        ciphertext.append(pow(char, e, n))
    print("Ciphertext: {}".format(ciphertext))
    print()

    decrypted_text = ""
    for i in ciphertext:
        decrypted_text += chr(pow(i, d, n) + 65)
    print("Decrypted Text: {}".format(decrypted_text))
    print()


def main():
    plaintext = input("Enter the plaintext: ")
    plaintext = plaintext.upper()
    e, d, n = keygen()
    RSA(plaintext, e, d, n)


if __name__ == "__main__":
    main()
