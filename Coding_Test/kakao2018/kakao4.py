def dfs(n,p,visit):
    result = 0
    if p > n:
        return 1
    else:
        for i in range(1,n+1):
            if (visit[i] == 0 )and (p %i == 0 or i % p ==0):
                visit[i] = 1
                result += dfs(n,p+1,visit)
                visit[i] = 0
    return result
visit = [0 for i in range(8)]
print(dfs(7,1,visit))
