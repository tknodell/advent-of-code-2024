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

with open('example', 'r') as file:
    for line in file:
        line = line.strip()
        stones = line.split(' ')
        stones = list(map(int, stones))

    print(stones)

    originalStones = stones.copy()

    for index, stone in enumerate(originalStones):
        print("Checking ", stone)
        if stone == 0:
            stones[index] = 1
            print("Change to 1")
        elif evenNumDigits(stone):
            res_first, res_second = split_digits(stone)

            stones[index:index+1] = [res_first,res_second]
            print("Insert two new stones", res_first, res_second)
        else:
            stones[index] = (stone * 2024)
            print("Multiply by 2024")
        print(stones)
        print()


    print(stones)
    # for i in range(1,6):
    #     print(i)
