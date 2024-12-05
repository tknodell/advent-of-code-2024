from collections import defaultdict

before_after = defaultdict(list)

with open('example-1', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split('|')

        beforenum = int(parts[0])
        afternum = int(parts[1])

        before_after[beforenum].append(afternum)


def isValid(num, arr):
    nums_to_check = arr[num]
    arr.remove(num)
    print(nums_to_check)


nums_to_check=(75,47,61,53,29)

for index,num in enumerate(nums_to_check):
    current_num = nums_to_check[index]
    print(current_num)
