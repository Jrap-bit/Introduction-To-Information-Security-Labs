import primegen as pg
import random


def gcd(k, q):
    if q == 0:
        return k
    else:
        return gcd(q, k % q)


def choose_k(prime):
    while True:
        k = random.randint(1, prime)
        if gcd(k, prime - 1) == 1:
            return k
        else:
            continue


def sign(message, prime, secret, gen):
    k = choose_k(prime)
    s1 = pow(gen, k, prime)
    inv_k = pow(k, -1, prime - 1)
    s2 = inv_k * (message - (secret * s1)) % (prime - 1)

    print("Chosen K: {}".format(k))
    print("S1: {}".format(s1), end=" ")
    print("S2: {}".format(s2), end=" ")
    return s1, s2


def verify(message, gen, prime, public, sign_arr, index):
    s1, s2 = sign_arr[index]
    v1 = pow(gen, message, prime)
    temp_1 = pow(public, s1)
    temp_2 = pow(s1, s2)
    v2 = (temp_1 * temp_2) % prime

    print("V1: {}".format(v1), end=" ")
    print("V2: {}".format(v2), end=" ")
    return v1, v2


def conv_message_to_arr(message):
    func_mess = message.upper()
    message_arr = []
    for i in func_mess:
        message_arr.append(ord(i) - 65)
    return message_arr


def main():
    inp_message = input("Enter the message: ")
    mess_arr = conv_message_to_arr(inp_message)
    q = pg.main(8)
    a = random.randint(1, q)
    xA = random.randint(1, q)
    public_key = pow(a, xA, q)

    print("Prime Number: {}".format(q), end=" ")
    print("a: {}".format(a), end=" ")
    print("xA: {}".format(xA), end=" ")
    print("Public Key: {}".format(public_key), end=" ")

    sign_arr = []
    index = 0

    for message in mess_arr:
        s1, s2 = sign(message, q, xA, a)
        print("Signatures for {}: [{},{}]".format(chr(message + 65), s1, s2))
        sign_arr.append([s1, s2])

    for message in mess_arr:
        v1, v2 = verify(message, a, q, public_key, sign_arr, index)
        print("Verification for {}: [{},{}]".format(chr(message + 65), v1, v2))
        index += 1
        if v1 == v2:
            print("Successfully Verified {} !".format(chr(message + 65)))


if __name__ == "__main__":
    main()
