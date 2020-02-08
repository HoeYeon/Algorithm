row_check = [[0,2],[],[0,1,2],[0,1,2],[1],[0,1,2],[0,1,2],[0,],[0,1,2],[0,1,2]]
col_check = [[0,1,2,3],[1,3],[1,2],[1,3],[0,1,3],[0,3],[0,2,3],[1,3],[0,1,2,3],[0,1,3]]

n,m = map(int,input().split())
m = str(m)
mid = n+1
result = ''
for i in range(2*n+3):
    for j in range(len(m)):
        if i == 0 or i == mid or i == mid*2:
            result += ' ' + '-'*n + ' ' if i//mid in row_check[int(m[j])] else ' '*(n+2)
        elif 0<i<mid:
            tmp = ('|'+' '*n if 0 in col_check[int(m[j])] else ' '*(n+1)) + ('|' if 1 in col_check[int(m[j])] else ' ')
            result += tmp
        elif mid<i<2*n+2:
            tmp = ('|'+' '*n if 2 in col_check[int(m[j])] else ' '*(n+1)) + ('|' if 3 in col_check[int(m[j])] else ' ')
            result += tmp
        result += ' '
    result += '\n'
print(result[:-1])

            
        


