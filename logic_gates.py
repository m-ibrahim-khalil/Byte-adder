
def half_adder(a, b):
    sum = a ^ b
    carry_bit = a & b
    return sum, carry_bit


def full_adder(a, b, carry_bit):
    sum1, carry_bit1 = half_adder(a, carry_bit)
    sum, carry_bit2 = half_adder(sum1, b)
    carry_bit = carry_bit1 | carry_bit2
    return sum, carry_bit


def binary_adder(a, b):
    bits_a = string_to_bits(a)
    bits_b = string_to_bits(b)

    res = []
    carry_bit = 0

    for i in range(len(bits_a)-1, -1, -1):
        sum, carry_bit = full_adder(bits_a[i], bits_b[i], carry_bit)
        res.append(sum)
    res.append(carry_bit)
    res.reverse()

    return ''.join(str(x) for x in res)


def string_to_bits(a):
    return [int(x) for x in a]
