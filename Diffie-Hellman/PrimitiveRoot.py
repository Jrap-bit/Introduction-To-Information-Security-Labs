# Optimized Method

def primefactors(s):
    factors = []
    c = 2
    for i in range(2, s):
        if s % i == 0:
            factors.append(i)
            s = s / i
        else:
            c = c + 1
    return factors


def primitiveroot(prime):
    s = prime - 1
    factors = primefactors(s)
    primitiveroots = []
    for i in range(2, prime):
        for j in factors:
            if pow(i, s // j, prime) == 1:
                break
        else:
            primitiveroots.append(i)
    return primitiveroots


def main(prime=7873):
    return primitiveroot(prime)


# Brute Force Method

# def primitiveRoot(base, p):
#     vals = set()
#     ret_val = False
#     for x in range(1, p):
#         if pow(base, x, p) not in vals:
#             vals.add(pow(base, x, p))
#         elif pow(base, x, p) in vals:
#             return ret_val
#
#     ret_val = True
#
#     for i in range(1, p):
#         if i not in vals:
#             ret_val = False
#
#     return ret_val
#
#
#
# def main(p=17):
#     primitive_roots = []
#     for i in range(2, p):
#         if primitiveRoot(i, p):
#             primitive_roots.append(i)
#     return primitive_roots


if __name__ == "__main__":
    main()
