import sys

input = sys.stdin.readline

N = int(input())
li = sorted([list(map(int,input().split())) for i in range(N)],key=lambda x : x[1])
print(li)