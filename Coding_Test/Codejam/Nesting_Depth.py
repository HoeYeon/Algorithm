import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    s = input()[:-1]
    result = '('*int(s[0])+s[0]

    for i, v in enumerate(s):
        if len(s) == 1:
            break
        if i != 0 and v == s[i-1]:
            result += v
            if i != len(s)-1 and v != s[i+1]:
                result += '('*(int(s[i+1]) - int(v))
            continue
        if i != 0:
            result += ')'*(int(s[i-1])-int(v))+v
        if i != len(s)-1:
            result += '('*(int(s[i+1]) - int(v))
    result += ')'*int(v)
    print('Case #{}: {}'.format(_+1, result))
