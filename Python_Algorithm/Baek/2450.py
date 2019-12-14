# 8
# 1 3 3 2 1 1 3 2

# 2

import itertools

N = int(input())
li = list(map(int, input().split()))

tmp = list(map(list, itertools.permutations([1, 2, 3])))
