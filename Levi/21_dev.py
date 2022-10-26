# exponent function - allows us to take a certain number and raise it to a specific power

# print(2**3)

# def raise_to_power(base_num, power_num):
#     result = 1
#     for index in range(power_num):
#         result = result * base_num
#     return result

# print(raise_to_power(3,6))

def raisse(base, pow):
    multiplier = 1
    for index in range(pow):
        multiplier = multiplier * base
    return multiplier

print(raisse(3,2))