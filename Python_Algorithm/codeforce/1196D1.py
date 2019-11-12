for _ in range(int(input())):
    n,k = map(int,input().split(' '))
    s = input()
    t = 'RGB'
    result = 99999999
    for i in range(n-k+1):
        for j in range(3):
            c = 0
            for q in range(k):
                if s[i+q] != t[(j+q)%3]:
                    c += 1
            result = min(result,c)
    print(result)
