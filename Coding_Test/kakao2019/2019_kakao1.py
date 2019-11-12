s = input()
length = len(s)//2
answer = 9999
#length 가 0이ㅣ 될때까지 실행하기
tmp = length
while length:
    li = [s[i:i+length] for i in range(0,len(s),length)]
    print(li)
    result = []
    count = 1
    for i in range(len(li)-1):
        if li[i] == li[i+1]:
            count+=1
            if i == len(li)-2:
                result.append(str(count)+li[i])
        else:
            result.append(str(count)+li[i]) if count != 1 else result.append(li[i])
            count = 1
            if i == len(li) -2:
                result.append(li[i+1])
    result = "".join(result)
    answer = min(answer,len(result))
    length -=1
if answer == 9999:
    answer = 1
print(answer)
