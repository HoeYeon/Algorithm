N,M = map(int,input().split(' '))
one = []
six = []
one_min = 9999
six_min = 9999
for i in range(M):
    a,b = map(int, input().split(' '))
    six.append(a)
    one.append(b)
six.sort()
one.sort()
one_min = one[0]
six_min = one[0] * 6
if six[0] < one[0]*6:
    six_min = six[0]
result = min((N//6)*six_min + (N%6)*one_min,(N//6+1)*six_min)
print(result)
