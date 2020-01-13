import heapq
import sys
input = sys.stdin.readline
minH=[]
maxH=[]
heapq.heapify(minH)
heapq.heapify(maxH)
n=int(input())
result = ''
while n:
    m=int(input())
    if len(minH)==len(maxH):
        heapq.heappush(maxH,(-m,m))
    else:
        heapq.heappush(minH,m)
    if (len(minH)!=0 and len(maxH)!=0) and maxH[0][1] > minH[0]:
        a=heapq.heappop(maxH)[1]
        b=heapq.heappop(minH)
        heapq.heappush(minH,a)
        heapq.heappush(maxH,(-b,b))
    result += str(maxH[0][1]) + '\n'
    n-=1
print(result)