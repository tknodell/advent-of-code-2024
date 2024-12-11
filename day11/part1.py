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

    for index in range(len(stones)):
        print("Checking ", stones[index])
        if stones[index] == 0:
            stones[index] = 1
            print("Change to 1")
        elif evenNumDigits(stones[index]):
            res_first, res_second = split_digits(stones[index])

            stones.insert(index-1,int(res_first))
            stones.insert(index+1,int(res_second))
            stones.pop(index)
            print("Insert two new stones", res_first, res_second)
        else:
            stones[index] = stones[index] * 2024
            print("Multiply by 2024")
        print(stones)
        print()


    print(stones)
    # for i in range(1,6):
    #     print(i)
