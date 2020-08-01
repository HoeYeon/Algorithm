kim = list(map(int, input().split()))
lee = list(map(int, input().split()))

ans = ""
debt = 0
for i in range(len(kim)):
    if kim[i] > lee[i]:
        debt = kim[i] - lee[i] - debt
        ans += str(debt) + " " if debt > 0 else "0 "
        debt = abs(debt) if debt < 0 else 0
    else:
        debt += lee[i] - kim[i]
        ans += "0 "
print(ans)
