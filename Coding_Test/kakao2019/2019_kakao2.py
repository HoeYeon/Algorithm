def check_perfect(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] == '(':
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False
def rev(s):
    tmp = ''
    for i in s:
        tmp = tmp+'(' if i==')' else tmp+')'
    return tmp

def func(s):
    if len(s) == 0:
        return s
    count = 1 if s[0] =='(' else -1
    u = s[0]
    v = ''
    for i in range(1,len(s)):
        if count == 0:
            v = s[i:]
            break
        count = count+1 if s[i] == '(' else count-1
        u = u+s[i]
    if check_perfect(u):
        return u + func(v)
    else:
        tmp = '('
        tmp = tmp + func(v)
        tmp = tmp + ')'
        u = u[1:-1]
        u = rev(u)
        tmp = tmp + u
        return tmp
print(func('(()())()'))
