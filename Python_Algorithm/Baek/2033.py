N = list(input())
n = int(''.join(N))
k = 1
while 10**k < n:
    if int(N[-k]) > 4:
        N[-k-1] = str(1 + int(N[-k-1]))
    N[-k] = '0'
    k += 1
    n = int(''.join(N))
print(n)