x =[0,0,0]
y =[0,0,0]
for i in range(3):
    x[i],y[i] = map(int,input().split())
x.sort()
y.sort()
print(x[0] if x[0] != x[1] else x[2], y[0] if y[0] != y[1] else y[2])
