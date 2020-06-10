# from copy import deepcopy


# def setRow(page1, page2, which):
#     page1[which][0], page1[which][1], page1[which][2] = page2[which][0], page2[which][1], page2[which][2]


# def setRow2(page1, page2, which):
#     page1[which][0], page1[which][1], page1[which][2] = page2[which][2], page2[which][1], page2[which][0]


# def setCol(page1, page2, which):
#     page1[0][which], page1[1][which], page1[2][which] = page2[0][which], page2[1][which], page2[2][which]


# def setCol2(page1, page2, which):
#     page1[0][which], page1[1][which], page1[2][which] = page2[2][which], page2[1][which], page2[0][which]


# def getCol(p):
#     return p[0][0], p[0][1], p[0][2]


# # U, D, F, B, L, R
# # 0, 1, 2, 3, 4, 5
# # w, y, r, o, g, b
# T = int(input())
# for i in range(T):
#     cube = [[['w' for i in range(3)] for j in range(3)],
#             [['y' for i in range(3)] for j in range(3)],
#             [['r' for i in range(3)] for j in range(3)],
#             [['o' for i in range(3)] for j in range(3)],
#             [['g' for i in range(3)] for j in range(3)],
#             [['b' for i in range(3)] for j in range(3)]]
#     n = int(input())
#     cmd = input().split()
#     for k in cmd:
#         page, direction = k[0], k[1]
#         if (page == 'U' and direction == '+'):
#             tmp = deepcopy(cube[4])
#             setRow2(cube[4], cube[2], 0)
#             setRow(cube[2], cube[5], 0)
#             setRow2(cube[5], cube[3], 0)
#             setRow(cube[3], tmp, 0)
#             # cube[3][0][:], cube[5][0][:], cube[2][0][:], cube[4][0][:
#             #                                                         ] = cube[4][0][:], cube[3][0][:], cube[5][0][:], cube[2][0][:]
#         elif (page == 'U' and direction == '-'):
#             tmp = deepcopy(cube[5])
#             setRow(cube[5], cube[2], 0)
#             setRow2(cube[2], cube[4], 0)
#             setRow(cube[4], cube[3], 0)
#             setRow2(cube[3], tmp, 0)
#             # cube[3][0][:], cube[4][0][:], cube[2][0][:], cube[5][0][:
#             #                                                         ] = cube[5][0][:], cube[3][0][:], cube[4][0][:], cube[2][0][:]

#         elif (page == 'D' and direction == '+'):
#             cube[3][2][:], cube[4][2][:], cube[2][2][:], cube[5][2][:
#                                                                     ] = cube[5][2][:], cube[3][2][:], cube[4][2][:], cube[2][2][:]
#         elif (page == 'D' and direction == '-'):
#             cube[3][2][:], cube[5][2][:], cube[2][2][:], cube[4][2][:
#                                                                     ] = cube[4][2][:], cube[3][2][:], cube[5][2][:], cube[2][2][:]

#         elif (page == 'F' and direction == '+'):
#             cube[0][2][:], [cube[5][0][0], cube[5][1][0], cube[5][2][0]], cube[1][2][:], [cube[4][0][0], cube[4][1][0], cube[4][2][0]] = \
#                 [cube[4][0][0], cube[4][1][0], cube[4][2][0]], cube[0][2][:], \
#                 [cube[5][0][0], cube[5][1][0], cube[5][2][0]], cube[1][2][:]
#         elif (page == 'F' and direction == '-'):
#             cube[0][2][:], [cube[4][0][0], cube[4][1][0], cube[4][2][0]], cube[1][2][:], [cube[5][0][0], cube[5][1][0], cube[5][2][0]] = \
#                 [cube[5][0][0], cube[5][1][0], cube[5][2][0]], cube[0][2][:], \
#                 [cube[4][0][0], cube[4][1][0], cube[4][2][0]], cube[1][2][:]

#         elif (page == 'B' and direction == '+'):
#             cube[0][0][:],  [cube[4][0][2], cube[4][1][2], cube[4][2][2]], cube[1][0][:], [cube[5][0][2], cube[5][1][2], cube[5][2][2]] = \
#                 [cube[5][0][2], cube[5][1][2], cube[5][2][2]], cube[0][0][:],  \
#                 [cube[4][0][2], cube[4][1][2], cube[4][2][2]], cube[1][0][:]
#         elif (page == 'B' and direction == '-'):
#             cube[0][0][:],  [cube[5][0][2], cube[5][1][2], cube[5][2][2]], cube[1][0][:], [cube[4][0][2], cube[4][1][2], cube[4][2][2]] = \
#                 [cube[4][0][2], cube[4][1][2], cube[4][2][2]], cube[0][0][:],  \
#                 [cube[5][0][2], cube[5][1][2], cube[5][2][2]], cube[1][0][:]

#         elif (page == 'L' and direction == '+'):
#             tmp = deepcopy(cube[3])
#             setCol(cube[3], cube[1], 0)
#             setCol2(cube[1], cube[2], 0)
#             setCol(cube[2], cube[0], 0)
#             setCol2(cube[0], tmp, 0)
#         elif (page == 'L' and direction == '-'):
#             tmp = deepcopy(cube[2])
#             setCol2(cube[2], cube[1], 0)
#             setCol(cube[1], cube[3], 0)
#             setCol2(cube[3], cube[0], 0)
#             setCol(cube[0], tmp, 0)

#         elif (page == 'R' and direction == '+'):
#             tmp = deepcopy(cube[2])
#             setCol2(cube[2], cube[1], 2)
#             setCol(cube[1], cube[3], 2)
#             setCol2(cube[3], cube[0], 2)
#             setCol(cube[0], tmp, 2)
#         elif (page == 'R' and direction == '-'):
#             tmp = deepcopy(cube[3])
#             setCol(cube[3], cube[1], 2)
#             setCol2(cube[1], cube[2], 2)
#             setCol(cube[2], cube[0], 2)
#             setCol2(cube[0], tmp, 2)
#         print("cmd: ", k)
#         for q in range(6):
#             print(cube[q])
#         print()
#     print(cube[0])

arr = [1, 2, 3, 4]
arr2 = [7, 4, 8, 2]
arr2[1] = arr[1]
arr2[1] = 12512
print(arr, arr2)
