from collections import deque
# from copy import deepcopy
# import sys
# input = sys.stdin.readline


# cctv = [[], [[0, 1]], [[0, 1], [-1, 0]], [[-1, 0], [0, 1]],
#         [[0, 1], [-1, 0], [0, -1]], [[0, 1], [0, -1], [-1, 0], [1, 0]]]

# # 오른쪽 90도


# def rot(cctv):
#     for i, v in enumerate(cctv):
#         if v == [0, 1]:
#             cctv[i] = [1, 0]
#         elif v == [-1, 0]:
#             cctv[i] = [0, 1]
#         elif v == [1, 0]:
#             cctv[i] = [0, -1]
#         elif v == [0, 1]:
#             cctv[i] = [0, 1]
#     return cctv


# def dfs(arr, cctvs, check, count):
#     global N
#     global M
#     # 영역 탐지
#     if count == len(cctvs):
#         tmp = deepcopy(arr)
#         for cctvInfo in cctvs:
#             x, y = cctvInfo['loc']
#             cctv = cctvInfo['cctv']
#             for way in cctv:
#                 _x, _y = way
#                 while 0 <= x+_x < N and 0 <= y+_y < N:
#                     if tmp[x+_x][y+_y] == 6:
#                         break
#                     if tmp[x+_x][y+_y] == 0:
#                         tmp[x+_x][y+_y] = '#'

#     for i, cctv in enumerate(cctvs['cctv']):
#         if check[i] == 0:
#             check[i] = 1
#             # rotate
#             for _ in range(4):
#                 cctvs['cctv'][i] = rot(cctv)
#                 dfs(arr, cctvs, check, count+1)

#             check[i] = 0


# N, M = map(int, input().split())
# cctvs = []
# arr = []
# for i in range(N):
#     li = list(map(int, input().split()))
#     for j, c in enumerate(li):
#         if c != 0 and c != 6:
#             cctvs.append({'loc': [i, j], 'cctv': cctv[c]})
#     arr.append(li)
# check = [[0 for i in range(M)] for j in range(N)]
# # print(cct