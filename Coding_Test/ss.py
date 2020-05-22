nums = {'I': 1, 'V': 5, 'X': 10}


def setNum(num):
    n = ''
    while num > 9:
        num %= 10
        n += 'X'
    if n == 4:
        return n+'IV'
    elif n == 9:
        return n+'IX'
    else:
        return n + num//5*'V' + (num % 5)*'I'


def getNum(num):
    count = 0
    i = 0
    while i < len(num) and num[i] == 'X':
        count += 10
        i += 1
    for j in range(i, len(num)):
        count = (abs(count - nums[num[j]]) if j != 0 and nums[num[j-1]]
                 < nums[num[j]]else count+nums[num[j]])
    return count


def solve():
    a, op, b = input().split()
    if op == '+':
        ans = getNum(a) + getNum(b)
    elif op == '-':
        if getNum(b) > getNum(a):
            return"작은 수에서 큰 수를 뺄 수 없습니다."
        ans = getNum(a) - getNum(b)
    elif op == '*':
        ans = getNum(a) * getNum(b)
    else:
        if getNum(b) > getNum(a):
            return"작은 수를 큰 수로 나눌 수 없습니다."
        print(
            f"몫 {setNum(getNum(a)//getNum(b))}, 나머지 {setNum(getNum(a) % getNum(b))}")
        return
    if ans > 39:
        return"범위를 벗어났습니다."
    else:
        return setNum(ans)


print(solve())
