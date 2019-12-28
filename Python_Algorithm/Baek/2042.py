import sys
from math import ceil,log
input = sys.stdin.readline

def makeTree(idx,start,end):
    if start == end:
        tree[idx] = li[start]
    else:
        tree[idx] = makeTree(idx*2,start,(start+end)//2) + makeTree(idx*2+1,(start+end)//2+1,end)
    return tree[idx]

def getSum(idx,start,end,want_left,want_right):
    if want_left > end or want_right < start:
        return 0
    elif want_left <= start and want_right >= end:
        return tree[idx]
    else:
        return getSum(idx*2,start,(start+end)//2,want_left,want_right) + getSum(idx*2+1,(start+end)//2+1, end, want_left, want_right)

def update(idx,start,end,target,diff):
    if target < start or target > end:
        return
    tree[idx] += diff
    if start != end:
        update(idx*2,start,(start+end)//2,target,diff)
        update(idx*2+1,(start+end)//2+1,end,target,diff)

N,M,K = map(int,input().split())
li = [int(input()) for i in range(N)]
tree_size = 2**(ceil(log(len(li),2))+1)
tree = [0 for i in range(tree_size)]
makeTree(1,0,N-1)
result = ''
for i in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        diff = c-li[b-1]
        li[b-1] = c
        update(1,0,N-1,b-1,diff)
    elif a == 2:
        result += str(getSum(1,0,N-1,b-1,c-1)) + '\n'
print(result)

