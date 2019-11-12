n = 5
# x,y,a,b
#xy는 좌표
# a ->0 기둥// 1-> 보
# b-> 0 삭제 // 1 -> 설치
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

#result == 1 보 result == 2 기둥
result = [[0] * (n+1) for _ in range(n+1)]
for i in build_frame:
    #설치
    if i[3] == 1:
        #print('설치')

        if i[2] == 0:
            #print('기둥')
            if i[1] == 0 or result[i[1]][i[0]] >= 1:
                result[i[1]+1][i[0]] += 2
                result[i[1]][i[0]] += 2

        elif i[2] == 1:
            #print('보')
            if result[i[1]][i[0]] >= 2 or result[i[1]][i[0]+1] >= 2 or (result[i[1]][i[0]] ==1 and result[i[1]][i[0]+1] == 1):
                result[i[1]][i[0]] += 1
                result[i[1]][i[0]+1] += 1

    elif i[3] ==0:
        #print('삭제')

        if i[2] == 0:
            #print('기둥')
            if result[i[1]+1][i[0]] == 0 or i[1] == 0:
                result[i[1]+1][i[0]] -= 2
                result[i[1]][i[0]] -= 2

        if i[2] == 1:
            #print('보')
            if result[i[1]-1][i[0]+1] >= 2 and result[i[1]-1][i[0]] >= 2:
                result[i[1]][i[0]] -= 1
                result[i[1]][i[0]+1] -= 1
ans = []
'''for i in result:
    print(i)'''
for i in range(len(result)):
    for j in range(len(result)):
        # 기둥점검
        if result[i][j] >1 and i != len(result) -1:
            ans.append([j,i,0,0])
            result[i][j] -= 2
            result[i+1][j] -= 2
        if result[i][j] >=1 and i != 0:
            ans.append([j,i,1,1])
            result[i][j] -= 1
            result[i][j+1] -= 1
ans.sort()
ans = [[:-1] for i in ans]
