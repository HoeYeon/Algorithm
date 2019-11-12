for i in range(int(input())):
    c_sum=0
    g_sum=0
    for j in range(int(input())):
        c,g = map(float,input().split(' '))
        c_sum += c
        g_sum += g*c
    print(int(c_sum),round(g_sum/c_sum,1)) # 소수점 1번째에서 반올림
    
