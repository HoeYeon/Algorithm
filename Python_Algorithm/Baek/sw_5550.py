for _ in range(int(input())):
    li = [0 for i in range(5)]
    ans = 0
    temp = 'roa'
    for i in input():
        if i == 'c':
            li[0]+=1
        elif i == 'r' or i == 'o' or i == 'a':
            if li[temp.index(i)] > li[temp.index(i)+1]:
                li[temp.index(i)+1]+=1
            else:
                ans = -1
                break
        else:
            if li[3] > 0:
                ans = max(max(li[0:4]),ans)
                li[0] -= 1
                li[1] -= 1
                li[2] -= 1
                li[3] -= 1
            else:
                ans = -1
                break
    if li[0]>0 or li[1] >0 or li[2] >0 or li[3] > 0:
        ans = -1
    print('#'+str(_+1),ans)
