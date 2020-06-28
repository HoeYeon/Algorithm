def isNum(li,length):
    if len(li) == length and li.isdigit():
        return True
    return False
def solution(phone_number):
    num = phone_number.split('-')
    
    # rule 2
    if len(num) == 1 and num[0][:3] == '010':
        rest_num = num[0][3:]
        if isNum(rest_num,8):
            return 2
        return -1
    # rule 1
    elif num[0] == '010' and len(num) == 3:
        if isNum(num[1],4) and isNum(num[2],4):
            return 1
        return -1
    # rule 3
    elif num[0] == '+82' and num[1] == '10' and len(num) == 4:
        if isNum(num[2],4) and isNum(num[3],4):
            return 3
        return -1
    else:
        return -1