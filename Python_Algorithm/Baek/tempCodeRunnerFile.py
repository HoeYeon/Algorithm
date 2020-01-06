C,K = map(int,input().split())
a = ['0']
a.extend(list(str(C)))
if len(a)-1 <= K:
    #1번째 반올림
    int(a[0]) += 1 if int(a[1]) >4 else 0
elif K == 1:
    #len-1 에서 반올림
    int(a[len(a)-2]) += 1 if int(a[len(a)-1]) > 4 else 0
else:
    #num-1에서 반올림
    int(a[K-2]) += 1 if int(a[K-1]) > 4 else 0
print(map(int,''.join(map(str,a))))