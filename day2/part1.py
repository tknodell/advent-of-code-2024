
numSafe = 0

def IncreaseAndDecrease(arr):
    increasing = all(int(arr[i]) <= int(arr[i + 1]) for i in range(len(arr) - 1))
    decreasing = all(int(arr[i]) >= int(arr[i + 1]) for i in range(len(arr) - 1))

    print(arr)
    print(increasing, decreasing)
    if not increasing and not decreasing:
        return True

with open('input', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(' ')

        safe = True

        if IncreaseAndDecrease(parts):
            safe = False
            print ("not safe increasing and decreasing")
            print(parts)

        for i in range(len(parts)-1):
            diff = abs(int(parts[i+1]) - int(parts[i]))
            print(diff)
            if diff > 3 or diff < 1:
                print("not safe")
                safe = False

        if safe:
            numSafe = numSafe + 1
        print("---")
        print(numSafe)
