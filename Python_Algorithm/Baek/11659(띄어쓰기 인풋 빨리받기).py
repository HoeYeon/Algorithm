from math import ceil,log
import sys
input = sys.stdin.readline
def init(idx,start,end):
    if start == end:
        tree[idx] = li[start]
    else:
        tree[idx] = init(idx*2,start,(start+end)//2) + init(idx*2+1,(start+end)//2+1,end)
    return tree[idx]

def getSum(idx,start,end,left,right):
    if left > end or right < start:
        return 0
    elif left <= start and right >= end:
        return tree[idx]

    return (getSum(idx*2,start,(start+end)//2,left,right) + 
    getSum(idx*2+1,(start+end)//2+1,end,left,right))
    
    
N,M = map(int,input().split())
li = list(map(int,input().split()))
h = ceil(log(N,2))
tree_size = 2**(h+1)
tree = [0 for i in range(tree_size)]
init(1,0,N-1)
result = ''
for i in range(M):
    a,b = map(int,input().split())
    result += str(getSum(1,0,N-1,a-1,b-1)) + ' '
print(result)