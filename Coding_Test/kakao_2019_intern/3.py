re = []
def dfs(li,b,idx):
    global re
    if idx == len(b):
        tt = li[:]
        re.append(tt)
        return
    for i in range(len(b[idx])):
        if b[idx][i] not in li:
            li.append(b[idx][i])
            dfs(li,b,idx+1)
            li.pop()

def solution(user_id, banned_id):
    answer = 0
    b = banned_id
    u = user_id
    ban = []
    tmp = []
    for i in range(len(b)):
        for j in range(len(u)):
            if len(b[i]) == len(u[j]):
                for k in range(len(b[i])):
                    if b[i][k] != '*' and b[i][k] != u[j][k]:
                        break
                    if k == len(b[i])-1:
                        tmp.append(u[j])
        ban.append(tmp)
        tmp = []
    dfs([],ban,0)
    cc = 0
    check = []
    for i in re:
        i = sorted(i)
        if len(set(i)) == len(ban) and i not in check:
            check.append(i)
            cc += 1
    return cc
