def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] != i:
                stack.pop()
            else:
                stack.append(i)
    answer = len(stack)
    return answer
