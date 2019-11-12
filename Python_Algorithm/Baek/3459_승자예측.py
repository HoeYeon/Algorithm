from math import pow

def get2(num):
    count = 0
    while num > 1:
        num = num // 2
        count += 1
    return count

T = int(input())
for _ in range(1,T+1):
    N = int(input())
    if N == 1:
        print('#'+str(_)+' Bob')
        continue
    elif N == 2 or N == 3:
        print('#'+str(_)+' Alice')
        continue
    count = get2(N)
    temp = 0
    temp2 = 1
    if count %2 == 0:
        while temp2 <= N:
            if temp %2 == 0:
                temp2 = temp2*2 + 1
            else:
                temp2 = temp2*2
            temp += 1
        if temp == count:
            print('#'+str(_)+' Alice')
        else:
            print('#'+str(_)+' Bob')
    else:
        while temp2 <= N:
            if temp %2 == 0:
                temp2 = temp2*2
            else:
                temp2 = temp2*2+1
            temp += 1
        if temp == count:
            print('#'+str(_)+' Bob')
        else:
            print('#'+str(_)+' Alice')
