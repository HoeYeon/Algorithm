def pit(start,ss,p):
    mid = start+2
    for j in range(5):
        l = mid  - (2- abs(2-j))
        r = mid + (2 - abs(2-j))
        for i in range(start,start+5):
            if j == 2 and i == mid:
                result[j][i] = ss
                continue
            if p == 'pit':
                if result[j][i] == '*':
                    continue
                result[j][i] = '#' if i==l or i==r else '.'
            else:
                result[j][i] = '*' if i==l or i==r else '.'
        
s = input()
result = [[0 for i in range(4*len(s)+1)] for j in range(5)]
for i in range(len(s)):
    pit(4*i,s[i],'pit') if (i+1)%3 != 0 else pit(4*i,s[i],'wen')
ans = ''.join(map(lambda x: ''.join(x)+'\n',result))
print(ans)