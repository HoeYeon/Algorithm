for j in range(int(input())):
    a,b = [[0 for i in range(26)] for j in range(2)]
    s,t,p = [input() for i in range(3)]
    check = True
    for i in s:
        a[ord(i)-97] += 1
    for i in t:
        b[ord(i)-97] += 1
    for i in p:
        a[ord(i)-97] += 1
    if len(s) > len(t):
        check = False
    else:
        cc = len(t)-1
        for i in range(len(s)-1,-1,-1):
            while t[cc] != s[i]:
                cc -= 1
                if cc < 0:
                    break
            cc-=1
        if cc < -1:
            check = False
    for i in range(len(a)):
        if a[i] < b[i]:
            check = False
    print('Yes' if check else 'No')
