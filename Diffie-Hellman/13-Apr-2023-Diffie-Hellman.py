from PrimitiveRoot import main as pr
import random

if __name__ == "__main__":
    prime = int(input("Enter a prime number: "))
    primitive = pr(prime)
    print("Primitive roots of", prime, "are:", primitive)
    chosen_primitive = int(input("Enter a primitive root: "))
    if chosen_primitive not in primitive:
        print("Not a primitive root!")
        exit()

    print("P = {}".format(prime))
    print("G = {}".format(chosen_primitive))

    # Xa = random.randint(1, prime)
    # Xb = random.randint(1, prime)

    Xa = int(input("Enter a secret number for Alice: "))
    Xb = int(input("Enter a secret number for Bob: "))

    Ya = pow(chosen_primitive, Xa, prime)
    Yb = pow(chosen_primitive, Xb, prime)

    print("Alice's public key: {}".format(Ya))
    print("Bob's public key: {}".format(Yb))

    Ka = pow(Yb, Xa, prime)
    Kb = pow(Ya, Xb, prime)

    print("Alice's shared secret: {}".format(Ka))
    print("Bob's shared secret: {}".format(Kb))