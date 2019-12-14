A, B, C = map(int, input().split())
ans = 1
tmp = A % C
while B > 0:
    if B % 2 == 1:
        ans *= tmp
        ans %= C
    tmp = ((tmp % C) * (tmp % C)) % C
    B //= 2
print(ans)

# 파이썬의 미친 기능
# pow(A,B,C) 를 하면 A의 B승을 C로 나눈 나머지 값...
