from collections import deque
T = int(input())
cube = [list(map(int, input().split())) for i in range(T)]


def u1(cube1):
    cube = cube1[:]
    cube[0], cube[1], cube[2], cube[3] = cube[1], cube[3], cube[0], cube[2]
    return cube


def u2(cube1):
    cube = cube1[:]
    cube[4], cube[5], cube[6], cube[7] = cube[5], cube[7], cube[4], cube[6]
    return cube


def d1(cube1):
    cube = cube1[:]
    cube[0], cube[1], cube[2], cube[3] = cube[2], cube[0], cube[3], cube[1]
    return cube


def d2(cube1):
    cube = cube1[:]
    cube[4], cube[5], cube[6], cube[7] = cube[6], cube[4], cube[7], cube[5]
    return cube


def r1(cube1):
    cube = cube1[:]
    cube[0], cube[1], cube[4], cube[5] = cube[1], cube[5], cube[0], cube[4]
    return cube


def r2(cube1):
    cube = cube1[:]
    cube[2], cube[3], cube[6], cube[7] = cube[3], cube[7], cube[2], cube[6]
    return cube


def l1(cube1):
    cube = cube1[:]
    cube[0], cube[1], cube[4], cube[5] = cube[4], cube[0], cube[5], cube[1]
    return cube


def l2(cube1):
    cube = cube1[:]
    cube[2], cube[3], cube[6], cube[7] = cube[6], cube[2], cube[7], cube[3]
    return cube


def check(cube):
    if cube[0] == cube[1] == cube[2] == cube[3]:
        return True
    elif cube[0] == cube[1] == cube[4] == cube[5]:
        return True
    elif cube[1] == cube[3] == cube[5] == cube[7]:
        return True
    return False


func_list = [u1, u2, d1, d2, r1, r2, l1, l2]

for i in cube:
    queue = deque([[i, 0]])
    while True:
        tmp = queue.popleft()
        cu, count = tmp[0], tmp[1]
        if check(cu):
            print("min_num: ", count)
            break
        for j in func_list:
            queue.append([j(cu), count+1])
