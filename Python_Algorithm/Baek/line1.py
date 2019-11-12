N = int(input())
w,h = 1,N
for i in range(1,int(N/2)):
    if N%i == 0:
        w = i
        h = N/w
        if w>=h:
            break
print(abs(int(w-h)))
