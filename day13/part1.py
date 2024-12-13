

def optimize(aX, aY, bX, bY, targetX, targetY):
    pressA, pressB, = 0,0

    while True:
        current_x = pressA * aX + pressB * bX
        current_y = pressA * aY + pressB * bY

        if current_x == targetX and current_y == targetY:
            return pressA, pressB

        if current_x < targetX:
            pressA += 1
        if current_x > targetX:
            pressB += 1
        if current_y < targetY:
            pressA += 1
        if current_y > targetY:
            pressB += 1

print(optimize(94,34,22,67,8400,5400))


# with open('example', 'r') as file:
#     for line in file:
#         print(line)
#         parts = line.split(':')


#         print(parts[0])


# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
