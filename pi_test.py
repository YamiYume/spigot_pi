from spigot import *


b = spigot_init(100)
size = len(b[0])
digits = []

while len(digits) < 100:
    b = radix_multiplication(b)
    for i in range(size - 1, 0, -1):
        b, _, _ = norm_per_digit(b, i)
    b, new_dig, _ = new_digit_gen(b)
    b = prov_digits_norm(b, new_dig)
    b, output = digits_emission(b, new_dig)
    digits += list(output)

print(digits)
