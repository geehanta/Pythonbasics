# takes a Number and allows raising to a power eg

# print(2**3)
base_num = int(input("Enter base number: "))
power_num = int(input("Raise to power?: "))


def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return int(result)


print(raise_to_power(base_num, power_num))
