record = ["RECEIVE abcd@naver.com", "RECEIVE zzkn@naver.com","DELETE", "RECEIVE qwerty@naver.com", "SAVE", "RECEIVE QwerTY@naver.com"]

tmp = []
save = []
for i in record:
    if i[0] =='R':
        cmnd,mail = i.split(' ')
    else:
        cmnd = i
    if cmnd == 'RECEIVE':
        tmp.append(mail)
    elif cmnd == 'SAVE':
        save = save + tmp
        tmp = []
    else:
        tmp.pop()
print(save)
