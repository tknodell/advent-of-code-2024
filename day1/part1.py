left_numbers_array = []
right_numbers_array = []

with open('input', 'r') as file:
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

# print(left_numbers_array)
# print(right_numbers_array)

i=0
sum=0
while i < len(left_numbers_array):
    if right_numbers_array[i] > left_numbers_array[i]:
        sum += right_numbers_array[i]-left_numbers_array[i]
    else:
        sum += left_numbers_array[i]-right_numbers_array[i]
    i=i+1

print(sum)
