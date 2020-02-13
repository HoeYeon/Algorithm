import sys
from collections import OrderedDict
input = sys.stdin.readline
N,M = map(int,input().split())
pokemon = OrderedDict({input()[:-1]:i for i in range(N)})
re = ''
for j in range(M):
    tmp = input()[:-1]
    re += list(pokemon.items())[int(tmp)-1][0]+'\n' if tmp.isdigit() else str(pokemon[tmp]+1) + '\n'
print(re)