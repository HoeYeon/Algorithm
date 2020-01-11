import sys
from math import log
input = sys.stdin.readline

def upCheck(start):
    while start//2 > 0:
        if arr[start] > arr[start//2]:
            arr[start],arr[start//2] = arr[start//2],arr[start]
            start //= 2
        else:
            break
def downCheck(idx):
    start = 1
    arr[start] = arr[idx]
    arr[idx] = 0
    while arr[start] != 0:
        tt = start*2 if arr[start*2] > arr[start*2+1] else start*2+1
        if arr[start] > arr[tt]:
            break
        arr[start],arr[tt] = arr[tt],arr[start]
        start = tt
    
    
def insert(data,idx):
    arr[idx] = data
    upCheck(idx)


N = int(input())
length = 2**(int(log(N,2))+1)
arr = [0 for i in range(length)]
idx = 1
result = ''
for i in range(N):
    tmp = int(input())
    if tmp == 0:
        result += str(arr[1]) +'\n'
        idx = 1 if idx == 1 else idx-1
        downCheck(idx)
    else:
        insert(tmp,idx)
        idx += 1

print(result)