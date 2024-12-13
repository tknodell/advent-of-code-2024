import numpy as np
import re

def parse_line(line):
    #Button A: X+62, Y+27
    x,y = line.split()[-2:]
    return int(x[2:-1]),int(y[2:])

def solveLinearMatrix(arr):

    aX = int(arr[0])
    aY = int(arr[1])
    bX = int(arr[2])
    bY = int(arr[3])
    prizeX = int(arr[4])
    prizeY = int(arr[5])

    prizeX += 10000000000000
    prizeY += 10000000000000

    A = np.array([[aX, bX], [aY, bY]])
    B = np.array([prizeX, prizeY])

    return np.linalg.solve(A,B)

def calcTokens(arr):
    res = solveLinearMatrix(arr)
    res = np.ndarray.round(res, 4)

    isValid = res[0].is_integer() and res[1].is_integer()
    if isValid:
        tokenA = res[0] * 3
        tokenB = res[1]
        return tokenA + tokenB
    else:
        return 0

totalTokens = 0
with open('input') as file:
    D = file.read()
    lines = D.split("\n\n")

    for line in lines:
        res = re.findall(r'\d+',line)
        numTokens = calcTokens(res)
        print(numTokens)
        totalTokens += numTokens

    print("---")
    print(totalTokens)
