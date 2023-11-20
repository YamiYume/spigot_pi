from spigot import *


b = spigot_init(1000)
size = len(b[0])
digits = []
cycle = 0

while len(digits) < 1000:
    cycle += 1
    b = radix_multiplication(b)
    for i in range(size - 1, 0, -1):
        b, _, _ , _= norm_per_digit(b, i)
    b, new_dig, _ = new_digit_gen(b)
    b = prov_digits_norm(b, new_dig)
    if new_dig == 10:
        print(cycle, 10)
    if new_dig == 9:
        print(cycle, 9)
    b, output = digits_emission(b, new_dig)
    if len(b[1]) > 2:
        print("multiple")
    digits += list(output)

print(digits)
