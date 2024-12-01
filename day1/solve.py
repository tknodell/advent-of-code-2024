left_numbers_array = []
right_numbers_array = []

with open('example', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split('   ')
        if len(parts) == 2:
            num1 = int(parts[0])
            num2 = int(parts[1])
            left_numbers_array.append(num1)
            right_numbers_array.append(num2)

left_numbers_array = sorted(left_numbers_array)
right_numbers_array = sorted(right_numbers_array)

print(left_numbers_array)
print(right_numbers_array)
