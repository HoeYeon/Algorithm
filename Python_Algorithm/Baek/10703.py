import sys

input = sys.stdin.readline
R, S = map(int, input().split())
arr = [list(input()) for i in range(R)]
colInfo = [
    {"s_start": -1, "s_end": -1, "g_start": R - 1, "g_end": R - 1} for i in range(S)
]
min_gap = R - 2
for i in range(S):
    # 유성찾기
    for j in range(R):
        if arr[j][i] == "#":
            break
        if colInfo[i]["s_start"] == -1 and arr[j][i] == "X":
            colInfo[i]["s_start"] = j
        if arr[j][i] == "X" and arr[j + 1][i] == ".":
            colInfo[i]["s_end"] = j

    # 땅 찾기
    for j in range(R - 1, -1, -1):
        if (colInfo[i]["s_start"] == -1 and colInfo[i]["s_end"] == -1) or (
            arr[j][i] == "X"
        ):
            break
        if arr[j][i] == "#" and arr[j - 1][i] == ".":
            colInfo[i]["g_end"] = j

    min_gap = min(colInfo[i]["g_end"] - colInfo[i]["s_end"] - 1, min_gap)

for i in range(S):
    if colInfo[i]["s_start"] != -1:
        for j in range(colInfo[i]["s_end"] - colInfo[i]["s_start"] + 1):
            (
                arr[colInfo[i]["s_end"] - j][i],
                arr[colInfo[i]["s_end"] + min_gap - j][i],
            ) = (
                arr[colInfo[i]["s_end"] + min_gap - j][i],
                arr[colInfo[i]["s_end"] - j][i],
            )
ans = ""
for i in range(R):
    ans += "".join(arr[i])
print(ans)
