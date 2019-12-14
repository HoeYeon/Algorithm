def getdiv(n):
    thr = n//2
    ans = 0
    for i in range(1,n+1):
        if i**2 > n:
            break
        else:
            if n % i == 0:
                ans += i
                if i**2 < n:
                    ans += n//i
    return ans

for i in range(int(input())):
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += getdiv(i)
    print(ans)
