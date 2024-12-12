def evenNumDigits(num):
    number_str = str(num)
    digits = len(number_str)
    return digits % 2 == 0

def split_digits(number):
    num_str = str(number)
    length = len(num_str)
    midpoint = length // 2

    first_half = num_str[:midpoint + (length % 2)]
    second_half = num_str[midpoint + (length % 2):]

    return first_half, second_half

def blink(stones):
    updatedStones = []
    for stone in stones:
        if stone == 0:
            updatedStones.append(1)
        elif evenNumDigits(stone):
            res_first, res_second = split_digits(stone)
            updatedStones.append(res_first)
            updatedStones.append(res_second)
        else:
            updatedStones.append(stone * 2024)
    return updatedStones


with open('example', 'r') as file:
    input = file.read()

stones = [int(n) for n in input.split()]

print(stones)

for i in range(1,6):
    print(blink(stones))
