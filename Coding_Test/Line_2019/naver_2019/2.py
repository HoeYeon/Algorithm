answer = 1
import itertools
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
li = list(map(str,li))
print(list(map(''.join, itertools.permutations(li, 2))))
