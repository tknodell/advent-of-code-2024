import numpy as np


def solveLinearMatrix(aX, aY, bX, bY, prizeX, prizeY):
    A = np.array([[aX, bX], [aY, bY]])
    B = np.array([prizeX, prizeY])

    # calulate inverse
    invA = np.linalg.inv(A)

    return invA @ B

    # OR you can do
    # return np.dot(invA, B)
    # return np.linalg.solve(A,B)

def calcTokens():
    # res = print(solveLinearMatrix(26,66,67,21,12748,12176))
    res = solveLinearMatrix(94,34,22,67,8400,5400)
    res = np.ndarray.round(res)


    isValid = res[0].is_integer() and res[1].is_integer()
    if isValid:
        tokenA = res[0] * 3
        tokenB = res[0]
        return tokenA + tokenB
    else:
        return 0

print(calcTokens)
