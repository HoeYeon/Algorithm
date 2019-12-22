from math import log,ceil
## 애들은 리프노드라고 생각하면 됨
a = [1,4,2,3,5,1,2,4,5,3]


'''만약, N이 2의 제곱꼴인 경우에는 Full Binary Tree 입니다.
또, 그 때 높이는 lgN 입니다.
리프 노드가 N개인 Full Binary Tree는 필요한 노드의 개수가 2*N-1개 입니다.

N이 2의 제곱꼴이 아닌 경우에는 높이가 H = lgN 이고,
총 세그먼트 트리를 만드는데 필요한 배열의 크기는 2^(H+1) - 1개가 됩니다.
'''
## 배열의 구간합을 편하게 구하기 위한 자료구조!
## 트리의 리프노드 --> 그 배열의 값 자체를 저장
## 트리의 다른 노드 --> 가지고 있는 자식의 합을 저장
## 재귀를 통해서 이런식으로 하면 리프 노드간 높이의 차이가 2 이상 나지 않게된다
## 예를 들어 그림과 같은 상황은 벌어지지 않음!
## 그래서 왼쪽자식은 (start,(start+end)//2)의 범위를 포함하고 오른쪽은 ((start+end)//2+1,end)를 포함하게 된다.
def init(idx,start,end):
    if start == end:
        try:
            tree[idx] = a[start]
        except:
            print(idx,start)
    else:
        tree[idx] = init(idx*2+1,start,(start+end)//2) + init(idx*2+2, (start+end)//2+1,end)
    return tree[idx]

N = len(a)
h = ceil(log(N,2))
## 2^(h+1)-1 과 같음
tree_size = (1 << (h+1))-1
tree = [0 for i in range(tree_size)]
print(tree_size)
init(0,0,N-1)
print(tree)
