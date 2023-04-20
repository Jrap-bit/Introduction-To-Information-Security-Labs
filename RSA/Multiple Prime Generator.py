import PrimeGen as pg

bit_4 = set()

for i in range(200):
    bit_4.add(pg.main(512))

print(bit_4)