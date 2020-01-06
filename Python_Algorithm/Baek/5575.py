for i in range(3):
    h1,m1,s1,h2,m2,s2 = map(int,input().split())
    h3,m3,s3 = h2-h1,m2-m1,s2-s1
    if s3 < 0:
        s3 += 60
        m3 -= 1
    if m3 < 0:
        m3 += 60
        h3 -= 1
    print(h3,m3,s3)
