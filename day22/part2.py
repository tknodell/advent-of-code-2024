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

def getPrice(number):
    numStr = str(number)
    strLen = len(numStr)
    return numStr[strLen-1]

def calc10(secretNum):
    initNum = secretNum
    for i in range(10):
        print(getPrice(secretNum))
        nextNum = calcNext(secretNum)
        secretNum = nextNum
        # print(secretNum)
        if i == 10-1:
            return secretNum

print(calc10(123))