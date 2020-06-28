def spinRight(gear):
    return [gear[-1], *gear[:-1]]


def spinLeft(gear):
    return [*gear[1:], gear[0]]


def spin(cond, gear):
    return spinRight(gear) if cond else spinLeft(gear)


def getAns(gears):
    score = 1
    ans = 0
    for i in gears:
        if i[0] == "1":
            ans += score
        score *= 2
    return ans


# 12 1 3 5 6 7 9 11
# 3시 -> idx:2, 9시 -> idx:6
gears = [list(input()) for i in range(4)]
K = int(input())
infos = [list(map(int, input().split())) for i in range(K)]
for info in infos:
    num, way = info
    num -= 1
    isSpin = [False for i in range(4)]
    isSpin[num] = True
    isClockWise = True if way == 1 else False
    # check Right
    for i in range(num, 3):
        if gears[i][2] != gears[i + 1][6]:
            isSpin[i + 1] = True
        else:
            break

    # check Left
    for i in range(num, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            isSpin[i - 1] = True
        else:
            break
    gears[num] = spin(isClockWise, gears[num])
    isClockWise = not isClockWise
    right, left = num + 1, num - 1
    while right < 4 or left > -1:
        if right < 4 and isSpin[right]:
            gears[right] = spin(isClockWise, gears[right])
        if left > -1 and isSpin[left]:
            gears[left] = spin(isClockWise, gears[left])
        isClockWise = not isClockWise
        right += 1
        left -= 1

print(getAns(gears))
