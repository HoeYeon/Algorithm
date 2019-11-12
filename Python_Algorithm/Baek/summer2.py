def mysol(li,cur,op,clo,n,cnt):
    if len(cur) == n*2:
        li.append(cur)
        return
    if op < n:
        cnt += 1
        mysol(li,cur+'(',op+1,clo,n,cnt)
    if clo < op:
        cnt += 1
        mysol(li,cur+')',op,clo+1,n,cnt)
def solution(N):
    answer = []
    li = []
    cur = ''
    mysol(li,cur,0,0,N,0)
    for i in li:
        answer.append(i)
    return answer
