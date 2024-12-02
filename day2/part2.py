
numSafe = 0

def IncreaseAndDecrease(arr):
    increasing = all(int(arr[i]) <= int(arr[i + 1]) for i in range(len(arr) - 1))
    decreasing = all(int(arr[i]) >= int(arr[i + 1]) for i in range(len(arr) - 1))

    # print(arr)
    # print(increasing, decreasing)
    if not increasing and not decreasing:
        return True

def diffIsSafe(arr):
    for i in range(len(arr)-1):
        diff = abs(int(arr[i+1]) - int(arr[i]))
        # print(diff)
        if diff > 3 or diff < 1:
            # print("not safe")
            return False


with open('example', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(' ')

        safe = True

        if IncreaseAndDecrease(parts):
            safe = False
            print ("not safe increasing and decreasing")
            # print(parts)

        if diffIsSafe(parts) == False:
            safe = False
            print ("not safe diff is too high")

        if not safe:
            print("origial one not safe")
            print(parts)
            for i in range(len(parts)-1):
                missingOne = parts.copy()
                missingOne.pop(i)

                if not IncreaseAndDecrease(missingOne) and diffIsSafe(missingOne):
                    safe = True
                    print ("now safe not increasing and decreasing and diff is good")
                    break

                missingOne = parts.copy

        if safe:
            numSafe = numSafe + 1
        print("---")
        print(numSafe)
