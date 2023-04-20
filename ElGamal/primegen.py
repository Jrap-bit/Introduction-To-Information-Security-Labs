import random


def rabin_miller(prime_candidate):
    even = prime_candidate - 1
    num_of_two = 0
    while even % 2 == 0:
        even >>= 1
        num_of_two += 1
    for i in range(10):
        a = random.randrange(2, prime_candidate - 1)
        x = pow(a, even, prime_candidate)
        if x == 1:
            return True
        for j in range(num_of_two - 1):
            x = pow(a, 2 ** j * even, prime_candidate)
            if x == 1:
                return True
            if x == prime_candidate - 1:
                return True
        else:
            return False


def prime_gen(n):
    first_primes_list = [2, 3, 5, 11, 7, 13, 17, 19, 23, 29,
                         31, 37, 41, 43, 47, 53, 59, 61, 67,
                         71, 73, 79, 83, 89, 97, 101, 103,
                         107, 109, 113, 127, 131, 137, 139,
                         149, 151, 157, 163, 167, 173, 179,
                         181, 191, 193, 197, 199, 211, 223,
                         227, 229, 233, 239, 241, 251, 257,
                         263, 269, 271, 277, 281, 283, 293,
                         307, 311, 313, 317, 331, 337, 347, 349]

    while True:
        n_bit_prime = random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)
        for i in first_primes_list:
            if n_bit_prime == i:
                return n_bit_prime
            if n_bit_prime % i == 0:
                break
        else:
            return n_bit_prime


def main(n=512):
    if n == 2:
        return random.choice([2, 3])
    while True:
        prime_cand = prime_gen(n)
        if not rabin_miller(prime_cand):
            continue
        else:
            return prime_cand


if __name__ == "__main__":
    main()
