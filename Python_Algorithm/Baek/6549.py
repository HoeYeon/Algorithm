from math import ceil,log
import sys
sys.setrecursionlimit(10**6)

def init(idx,start,end):
    if start == end:
        tree[idx] = start
    else:
        init(idx * 2+1, start, (start+end)//2)
        init(idx*2+2, (start+end)//2+1, end)
        ## 세그먼트 트리를 활용하는데 저장하고자 하는 노드의 인덱스를 저장
        ## 자식 2개를 비교해서 더 작은 높이를 가진 노드의 인덱스를 저장
        tree[idx] = tree[idx*2+1] if li[tree[idx*2+1]] <= li[tree[idx*2+2]] else tree[idx*2+2]
    return tree[idx]

## start,end --> 현재 노드가 담당하고 있는 범위
## left, right --> 구해야 하는 합의 범위
## init함수가 자식중에 낮은 높이 가진애의 인덱스를 구하는 함수였다면
## 얘는 구간에서 가장 작은 높이 가진애의 인덱스를 구하는 함수
def query(idx,start,end,left,right):
    ## 노드가 담당하고 있는 거랑 상관이 없으면 탈출
    if left > end or right < start:
        return -1

    ## 노드가 담당하고 있는 거에 완전 포함되면 고대로 리턴
    elif left <= start and right >= end:
        return tree[idx]
    ## 트리를 내려가면서 최소 합 구해보기
    m1 = query(idx*2+1,start,(start+end)//2,left,right)
    m2 = query(idx*2+2,(start+end)//2+1,end,left,right)
    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    else:
        ## 자식중에 더 작은 높이를 가진 애를 리턴
        return m1 if li[m1] <= li[m2] else m2

# 이제 그럼 query함수를 통해 구간에서 가장 작은 높이를 구할 수 있으니 넓이를 구하자
def getMax(start,end):
    h = query(0,1,li[0],start,end)
    #print('h:',h)
    area = li[h] * (end-start+1)
    #print(area)
    if 0<start<=h-1:
        area = max(area,getMax(start,h-1))
    if end>=h+1:
        area = max(area,getMax(h+1,end))
    return area



while True:
    li = list(map(int,input().split()))
    if li[0] == 0:
        break
    h = ceil(log(li[0],2))
    ## 2^(h+1)-1 과 같음
    tree_size = (1 << (h+1))-1
    tree = [0 for i in range(tree_size)]
    tree[0] = 999999999999999
    init(0,1,li[0])
    print(tree)
    print(getMax(1,li[0]))
