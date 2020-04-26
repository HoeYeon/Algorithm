import sys
input = sys.stdin.readline

N = int(input())
score = sorted([int(input()) for i in range(N)], reverse=True)
max_score = 0
result = 0
for i, v in enumerate(score):
    result += (v+N >= max_score)
    max_score = max(max_score, v+i+1)
print(result)
