def solution(history):
    answer = []
    ref = [5,100,10,5,2]
    recipe = [4,50,10,10,4]
    price = [10000,3000,1000,2000,1000]
    add = [10,100,30,50,10]

    for i in history:
        tmp = 0
        i = float(i)
        if i > 2.5 or i<1.0:
            return [-1]
        recipe[4] = 2 if (i == 1.5 or i == 2.5) else 4
        food = recipe[:]
        food = [int(k*i) for k in food]
        for j in range(5):
            while ref[j] < food[j]:
                ref[j] += add[j]
                tmp += price[j]
            ref[j] -= food[j]
        answer.append(tmp)
    return answer
