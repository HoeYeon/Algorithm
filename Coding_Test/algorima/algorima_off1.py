f = open('input.txt', 'r')
N = f.readline()
task = [list(map(float, f.readline()[:-1].split())) for i in range(int(N))]
f.close()

# k[0] 오븐가격, k[1] 새 오븐 생산량, k[2] 원하는 피자
f = open('output.txt','w')
count = 1
for k in task:
    price, oven, pizza = k[0], k[1], k[2]
    print('info: ', price, oven, pizza)
    make = 2.0
    # 처음 시작은 가장 기본 오븐만 사용했을때
    start = pizza/make
    i = 0
    # 계속해서 새 오븐을 구입해보면서 기존의 방법과 비교
    # 만약 기존의 방법이 더 빠르다면 탈출해서 출력
    B_price = 0
    while True:
        # 새 오븐을 계속 추가했을 때 시간
        B_price += price/(make+(i*oven))
        # 모든 오븐을 사용해서 전체 피자 만들었을때 시간
        tot = pizza/(make+((i+1)*oven))
        tot += B_price
        # 기존의 방법이 더 빠르면 탈출
        if start < tot:
            break
        # 아니라면 기존의 방법을 업데이트 하고 반복
        start = tot
        i += 1
    print(start)
    f.write('Case #'+str(count)+': '+str(start)+'\n')
    count += 1
f.close()
