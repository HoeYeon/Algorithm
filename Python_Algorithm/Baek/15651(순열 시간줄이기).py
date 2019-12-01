from itertools import permutations,product

N,M = map(int,input().split())
arr = [str(i) for i in range(1,N+1)]
'''li = list(map(list,product(arr,repeat=M)))
for i in li:
    print('\n'.join(i))'''
li = list(map(' '.join,product(arr,repeat=M)))
print(li)
print('\n'.join(li))
## 위 방법 보다 아래 방법이 6배는 빠르다
## print를 최대한 적게 써야 시간이 빠르다
