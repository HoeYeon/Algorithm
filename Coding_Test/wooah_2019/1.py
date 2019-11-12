def solution(restaurant, riders, k):
    answer = 0
    for i in riders:
        tmp = (i[0]-restaurant[0])*(i[0]-restaurant[0]) + (i[1]-restaurant[1])*(i[1]-restaurant[1])
        if tmp < k**2:
            answer+=1
    return answer
