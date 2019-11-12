import itertools

pool = ['a','b','c']

a = list(map(list,itertools.permutations(pool)))
# 여기부터
# 곱해서 최대인거 찾기
print(a)
