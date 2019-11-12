'''from functools import reduce
li = [1,2,3,4,5]
print(reduce(lambda x,y:x*y, li))
'''
 # 120 = ((((1*2)*3)*4)*5)


stack = [1]
add_tmp = 0
result = 0
tmp = 0
cc = 0
check = True
li = [0 for i in range(100001)]
for _ in range(int(input())):
    comnd = input().split(' ')
    if comnd[0] == 'for':
        num = comnd[1]
        stack.append(num)
        cc += 1
    elif comnd[0] == 'add':
        if cc == 0:
            li[cc] += 1
        else:
            stack.append('add')
    elif comnd[0] == 'end':
        a = stack.pop()
        while a.isalpha():
            #add_tmp += 1
            li[cc] += 1
            a = stack.pop()
        cc -= 1
        a = int(a)
        li[cc] = li[cc] + li[cc+1]*a
        li[cc+1] = 0
        if li[cc] >= 2**32:
            check = False
            break
        #add_tmp = a*add_tmp
        '''if cc == 0:
            result += add_tmp
            add_tmp = 0'''

if li[0] >= 2**32 or check == False :
    #print(result)
    print("OVERFLOW!!!")
else:
    #print(result)
    print(li[0])



'''8
for 2
for 3
add
end
for 4
add
end
end'''
