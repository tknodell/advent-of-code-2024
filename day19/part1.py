
file =  open('example', 'r')
first_line = file.readline().strip()

avaiableTowels = first_line.split(",")
print(avaiableTowels)


file =  open('example', 'r')
content = file.readlines()

patterns = content[3:]

validPatterns=0

for pattern in patterns:
    # print(pattern.strip())

    letters = list(pattern)

    print(len(letters))

    # for letter in letters:
    #     if letter not in avaiableTowels:
    #         # no match
    #         print(letter)



    # print(avaiableTowels)

    # for line in file:
    #     line = line.strip()
    #     parts = line.split(' ')
