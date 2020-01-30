from itertools import permutations
def getSum(li):
    return sum(map(lambda x,y: abs(x-y),li[:-1],li[1:]))
N = int(input())
li = list(map(list,permutations(map(int,input().split()))))
result = max(map(getSum,li))
print(result)