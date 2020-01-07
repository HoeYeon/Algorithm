import sys
from math import log,ceil
input = sys.stdin.readline
MAX = 1000000000
mmin = MAX+1
def make_min_tree(idx,start,end):
    if start == end:
        min_tree[idx] = arr[start]
    else:
        min_tree[idx] = min(make_min_tree(idx*2,start,(start+end)//2),make_min_tree(idx*2+1,(start+end)//2+1,end))
    return min_tree[idx]

def get_min(idx,wl,wr,start,end):
    if wr < start or wl > end:
        return MAX +1
    elif wl <= start and wr >= end:
        return min_tree[idx]
    else:
        mmin = min(get_min(idx*2,wl,wr,start,(start+end)//2),get_min(idx*2+1,wl,wr,(start+end)//2+1,end))
        return mmin

N,M = map(int,input().split())
arr = [int(input()) for i in range(N)]

h = ceil(log(N,2))
tree_size = 2**(h+1)
min_tree = [0 for i in range(tree_size)]
make_min_tree(1,0,N-1)
result = ''
for i in range(M):
    a,b = map(int,input().split())
    result += str(get_min(1,a-1,b-1,0,N-1)) +'\n'

print(result)