def union(start,d):
    try:
        li = []
        while True:
            li.append(start)
            start = d[start]
    except:
        for i in li:
            d[i] = start+1
        return d,start
def solution(k, room_number):
    re = []
    d = {}
    want = room_number
    for i in room_number:
        d,end = union(i,d)
        re.append(end)

    return re
'''def solution(k, room_number):
    answer = []
    want = room_number
    room = [0 for i in range(k)]
    for i in want:
        i -= 1
        if room[i] == 0:
            room[i] = 1
            answer.append(i+1)
            continue
        for j in range(i+1,k):
            if room[j] == 0:
                room[j] = 1
                answer.append(j+1)
                break
    return answer'''
