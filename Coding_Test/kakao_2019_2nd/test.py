import requests
import json

url = 'https://wqwfrkh5k1.execute-api.ap-northeast-2.amazonaws.com/kakao-2020/'

usr_list = {}
def start(url,pro):
    uri = url + '/start'
    return requests.post(uri, headers= {'X-Auth-Token':'a1df1d6cdb93aae229176379ba636f82'},data={'problem':pro}).json()

def user(url,tok):
    uri = url + '/users'
    return requests.get(uri, headers={'Authorization': tok}).json()

def recmnd(url,tok,recommend):
    uri = url + '/recommend'
    return requests.post(uri, headers={'Authorization': tok},json = {'recommendations':recommend})

def run(url,tok):
    uri = url + '/run_simulation'
    return requests.put(uri, headers={'Authorization': tok})

def stat(url,tok):
    uri = url + '/status'
    return requests.get(uri, headers={'Authorization': tok}).json()

def score(url,tok):
    uri = url + '/score'
    return requests.get(uri, headers={'Authorization': tok}).json()

def usr_set(usr):
    for i in usr:
        usr_list[i['user']] = {'following': i['following'], 'phone': i['phone']}

def c_num(usr,d):
    if usr in usr_list:
        for i in usr_list[usr]['phone']:
            #usr id 나오고
            if i not in usr_list[usr]['following']:
                d[i] = 1
            if i in usr_list:
                for j in usr_list[i]['following']:
                    d[j] = d[j] +1 if j in d else 1
        for i in usr_list[usr]['following']:
            #usr id 나오고
            if i in usr_list:
                for j in usr_list[i]['following']:
                    if j in usr_list[usr]['following']:
                        if j in d:
                            del d[j]
                        continue
                    d[j] = d[j] +1 if j in d else 1
    return d

tok = start(url,2)['token']
usr = user(url,tok)
usr = usr['users']

u = []
p = []
'''cnt = 0
for _ in range(1):
    for i in usr:
        u.append(i['user'])
        p.append(i['phone'])
        cnt += len(i['phone'])
        if cnt > 100:
            tmp1, tmp2 = u.pop(),p.pop()
            print('length of p',p)
            rec = [ {"user":k,"recommendation":v} for k,v in dict(zip(u,p[:10])).items()]
            print(recmnd(url,tok,rec))
            print(run(url,tok))
            cnt = len(tmp2)
            u = [tmp1]
            p = [tmp2]
'''
rec = []
tot = 0
cnt = 0
tmp_cnt = 0
for _ in range(100):
    '''if _ < 30:
        print(recmnd(url,tok,[{"user":"",'recommendation' : []}]))
        while stat(url,tok)['status'] == 'working':
            a = 1
        print(run(url,tok))
        continue'''
    '''tmp_cnt += 1
    if tmp_cnt == 10:
        usr = user(url,tok)['users']
        usr_set(usr)
        tmp_cnt = 0'''
    usr = user(url,tok)['users']
    usr_set(usr)
    for i in usr:
        if len(i['following']) >= 20:
            continue
        d = {}
        u = i['user']
        d = c_num(i['user'],d)
        dd = sorted(d.items(), key=lambda x: x[1],reverse = True)
        #print(dd[0][0], dd[0][1])
        p = dd[:10] if len(dd) > 10 else dd[:]
        if len(dd) == 0:
            continue
        p = [i[0] for i in p]
        tot += len(p)
        rec.append({"user":u,"recommendation":p})
        if tot > 1000:
            cnt += 1
            tmp1 = rec.pop()
            print('length!:',len(rec))
            print(recmnd(url,tok,rec))
            rec = [tmp1]
            tot = len(tmp1)
            while stat(url,tok)['status'] == 'working':
                a = 1
            print(run(url,tok))
        if cnt == 10:
            print(score(url,tok))
            cnt = 0
print(stat(url,tok))
print(score(url,tok))
