def solution(infos, actions):
    answer = []
    dd = {}
    for i in infos:
        a,b = i.split()
        dd[a] = b
    login_check = False
    ADD_check = False
    for i in actions:
        li = i.split()
        if li[0] == 'LOGIN':
            if login_check == True:
                answer.append(False)
            elif li[1] not in dd or dd[li[1]] != li[2]:
                answer.append(False)
            else:
                answer.append(True)
                login_check = True
        elif li[0] == 'ADD':
            if login_check == True:
                ADD_check = True
                answer.append(True)
            else:
                answer.append(False)
        elif li[0] == 'ORDER':
            if ADD_check == True:
                ADD_check = False
                answer.append(True)
            else:
                answer.append(False)
    return answer
