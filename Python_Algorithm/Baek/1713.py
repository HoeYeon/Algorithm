n = int(input())
num = int(input())

def is_in_arr(arr , w):
    for i in arr:
        if i[2] == w:
            return True
    return False

arr = []
who = input().split()
for idx, w in enumerate(who):
    if is_in_arr(arr, w):
        for i in arr:
            if i[2] == w:
                i[0] += 1
                break
    else:
        if len(arr) < n:
            arr.append([1, idx, w])
        else:
            arr[0] = [1, idx, w]

    arr.sort(key=lambda x: (x[0], x[1]))

arr.sort(key=lambda x:int(x[2]))
ans = ' '.join(map(lambda x: str(x[2]),arr))
print(ans)