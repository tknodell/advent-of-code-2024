def evenNumDigits(num):
    number_str = str(num)
    digits = len(number_str)
    return digits % 2 == 0

def blink(stones):
    updatedStones = []
    for stone in stones:
        if stone == 0:
            updatedStones.append(1)
        elif len(str(stone)) % 2 == 0:
            n = len(str(stone)) // 2
            a = int("".join(list(str(stone))[:n]))
            b = int("".join(list(str(stone))[n:]))
            updatedStones.append(a)
            updatedStones.append(b)
        else:
            updatedStones.append(stone * 2024)
    return updatedStones


with open('input', 'r') as file:
    input = file.read()

stones = [int(n) for n in input.split()]

# print(stones)

# print(blink(stones))

for i in range(75):
    stones = blink(stones)
    print(i)
    # print(stones)

print(len(stones))
