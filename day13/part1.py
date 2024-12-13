import numpy as np
import re

def parse_line(line):
    #Button A: X+62, Y+27
    x,y = line.split()[-2:]
    return int(x[2:-1]),int(y[2:])

def solveLinearMatrix(aX, aY, bX, bY, prizeX, prizeY):
    A = np.array([[aX, bX], [aY, bY]])
    B = np.array([prizeX, prizeY])

    # calulate inverse
    invA = np.linalg.inv(A)

    return invA @ B

    # OR you can do
    # return np.dot(invA, B)
    # return np.linalg.solve(A,B)

def calcTokens(arr):
    res = solveLinearMatrix(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5])
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
        numTokens = calcTokens([int(res[0]),int(res[1]),int(res[2]),int(res[3]),int(res[4]),int(res[5])])
        print(numTokens)
        totalTokens += numTokens

    print("---")
    print(totalTokens)
