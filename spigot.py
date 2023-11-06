from numpy import divmod
 
Buffer = tuple[list[int], list[int]]

def spigot_init(digits: int) -> Buffer:
    size = 10 * digits // 3 + 1
    digit_list = [2] * size
    prov_digits = []
    return digit_list, prov_digits

def radix_multiplication(b: Buffer) -> Buffer:
    digit_list, prov_digits = b
    digit_list = [10 * x for x in digit_list]
    return digit_list, prov_digits

def norm_per_digit(b: Buffer, position: int) -> tuple[Buffer, int, int]:
    if not position:
        raise Exception("position is 0")
    digit_list, prov_digits = b
    quot, rem = divmod(digit_list[position], 2 * position + 1)
    digit_list[position] = rem
    digit_list[position - 1] += quot * position
    b = (digit_list, prov_digits)
    return b, quot, rem

def new_digit_gen(b: Buffer) -> tuple[Buffer, int, int]:
    digit_list, prov_digits = b
    new_dig, rem = divmod(digit_list[0], 10)
    digit_list[0] = rem
    b = (digit_list, prov_digits)
    return b, new_dig, rem

def prov_digits_norm(b: Buffer, new_dig: int) -> Buffer:
    digit_list, prov_digits = b
    if new_dig == 10:
        prov_digits = [(x + 1) % 10 for x in prov_digits] + [0]
    else:
        prov_digits.append(new_dig)
    return digit_list, prov_digits

def digits_emission(b: Buffer, new_dig: int) -> tuple[Buffer, tuple[int]]:
    digit_list, prov_digits = b
    if new_dig == 10:
        digits_output = tuple(x for x in prov_digits[:-1])
        prov_digits = prov_digits[-1:]
    elif new_dig == 9:
        digits_output = tuple()
    else:
        digits_output = tuple(prov_digits[:-1])
        prov_digits = prov_digits[-1:]
    b = (digit_list, prov_digits)
    return b, digits_output

