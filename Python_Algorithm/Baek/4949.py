import sys
input = sys.stdin.readline
ans = ''
while True:
    s = input()[:-1]
    stack = []
    check = True
    if s == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                ans += 'no\n'
                check = False
                break
        elif i == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                ans += 'no\n'
                check = False
                break
        else:
            continue
    if check:
        ans += 'yes\n' if len(stack) == 0 else 'no\n'
print(ans)
