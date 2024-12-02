
numSafe = 0

def increasing_decreasing(nums):
    increasing = decreasing = True

    for i in range(1, len(nums)):
        if int(nums[i]) < int(nums[i - 1]):
            increasing = False
        if int(nums[i]) > int(nums[i - 1]):
            decreasing = False

    return increasing or decreasing


def diffIsSafe(arr):
    for i in range(1, len(arr)):
        diff = abs(int(arr[i]) - int(arr[i - 1]))
        if diff > 3 or diff < 1:
            return False

    return True

with open('input', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(' ')

        safe = True

        print("Checking", parts)
        if increasing_decreasing(parts) is False:
            safe = False
            print ("not safe increasing and decreasing")
            # print(parts)

        if diffIsSafe(parts) == False:
            safe = False
            print ("not safe diff is too high")

        if safe is False:
            print("original one not safe")
            print(parts)
            for i in range(0, len(parts)):
                missingOne = parts.copy()
                missingOne.pop(i)

                print(missingOne, increasing_decreasing(missingOne), diffIsSafe(missingOne))
                if increasing_decreasing(missingOne) and diffIsSafe(missingOne):
                    safe = True
                    print ("now safe not increasing and decreasing and diff is good")
                    break

        if safe:
            print(parts, " is safe")
            print()
            numSafe = numSafe + 1
        else:
            print(parts, " is not safe")
            print()
    print("---")
    print(numSafe)
