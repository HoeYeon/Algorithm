fin = []
def dfs(N,M,arr):
    if len(arr) == N:
        tmp = arr[:]
        fin.append(tmp)
        return
    for i in range(0,M+1):
        if sum(arr) + i <= M:
            arr.append(i)
            dfs(N,M,arr)
            arr.pop()
def check(fin,M,T,K):
    result = 0
    for i in fin:
        ch = True
        for j in range(len(i)-T+1):
            if sum(i[j:j+T]) > K:
                ch = False
                break
        if ch and sum(i) == M:
            result += 1
    return result
def solution(N,M,T,K):
    dfs(N,M,[])
    print(len(fin))
    ans = check(fin,M,T,K)
    return ans
solution(8,10,3,5)