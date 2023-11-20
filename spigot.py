from numpy import divmod
 
Buffer = tuple[list[int], list[int]]

def spigot_init(digits: int) -> Buffer:
    size = 10 * digits // 3 + 1
    spigot_list = [2] * size
    prov_digits = []
    return spigot_list, prov_digits

def radix_multiplication(b: Buffer) -> Buffer:
    spigot_list, prov_digits = b
    spigot_list = [10 * x for x in spigot_list]
    return spigot_list, prov_digits

def norm_per_digit(b: Buffer, position: int) -> tuple[Buffer, int, int, int]:
    if not position:
        raise Exception("position is 0")
    spigot_list = b[0].copy()
    prov_digits = b[1].copy()
    quot, rem = divmod(spigot_list[position], 2 * position + 1)
    spigot_list[position] = rem
    carry = quot * position
    spigot_list[position - 1] += carry
    b = (spigot_list, prov_digits)
    return b, quot, rem, carry

def new_digit_gen(b: Buffer) -> tuple[Buffer, int, int]:
    spigot_list = b[0].copy()
    prov_digits = b[1].copy()
    new_dig, rem = divmod(spigot_list[0], 10)
    spigot_list[0] = rem
    b = (spigot_list, prov_digits)
    return b, new_dig, rem

def prov_digits_norm(b: Buffer, new_dig: int) -> Buffer:
    spigot_list = b[0].copy()
    prov_digits = b[1].copy()
    if new_dig == 10:
        prov_digits = [(x + 1) % 10 for x in prov_digits] + [0]
    else:
        prov_digits.append(new_dig)
    return spigot_list, prov_digits

def digits_emission(b: Buffer, new_dig: int) -> tuple[Buffer, tuple[int]]:
    
    spigot_list = b[0].copy()
    prov_digits = b[1].copy()
    if len(prov_digits) <= 1:
        return (spigot_list, prov_digits), tuple()
    if new_dig == 10:
        digits_output = tuple(x for x in prov_digits[:-1])
        prov_digits = prov_digits[-1:]
    elif new_dig == 9:
        digits_output = tuple()
    else:
        digits_output = tuple(prov_digits[:-1])
        prov_digits = prov_digits[-1:]
    b = (spigot_list, prov_digits)
    return b, digits_output

def adv_by_cycles(b: Buffer, t: int) -> tuple[Buffer, tuple[int]]:
    output = []
    for _ in range(t):
        b = adv_subcycle(b)
        b, new_dig, _ = new_digit_gen(b)
        b = prov_digits_norm(b, new_dig)
        b, new_output = digits_emission(b, new_dig)
        output += new_output
    return b, output

def adv_subcycle(b: Buffer) -> Buffer
    b = radix_multiplication(b)
    for i in range(len(b[0]) - 1, 0, -1):
        b, _, _, _ = norm_per_digit(b, i)
    return b
    

