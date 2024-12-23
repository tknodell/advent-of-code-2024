import math

def mix(secretNum, numToMix):
    return secretNum ^ numToMix

def prune(secretNum):
    return secretNum % 16777216


def calcNext(secretNum):
    # step 1
    res1 = secretNum * 64
    res2 = mix(secretNum, res1)
    res3 = prune(res2)

    # step 2
    res4 = res3 / 32
    res5 = math.floor(res4)
    res6 = mix(res3, res5)
    res7 = prune(res6)

    # step 3
    res8 = res7 * 2048
    res9 = mix(res7, res8)
    res10 = prune(res9)

    return res10

def calc2000(secretNum):
    initNum = secretNum
    for i in range(2000):
        nextNum = calcNext(secretNum)
        secretNum = nextNum
        if i == 2000-1:
            return secretNum

# example mix and prune
# print(mix(42,15))
# print(prune(100000000))


# Testing result
testFinalSum = 0
for i in (1,10,100,2024):
    testFinalSum += calc2000(i)

print(testFinalSum)

finalSum = 0
with open('input', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split('\n')

        # print(line)
        finalSum += calc2000(int(line))

print(finalSum)
