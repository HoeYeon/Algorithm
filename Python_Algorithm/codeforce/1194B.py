for _ in range(int(input())):
  n,m=map(int,input().split())
  g=[input() for _ in range(n)]
  a=[0]*n
  b=[0]*m
  for i in range(n):
    for j in range(m):
      if '*'==g[i][j]:
        a[i]+=1
        b[j]+=1
  ans=0
  for i in range(n):
    for j in range(m):
      ans=max(ans,a[i]+b[j]-(g[i][j]=='*'))
  print(n+m-1-ans)
