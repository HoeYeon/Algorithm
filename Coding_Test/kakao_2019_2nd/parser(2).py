import requests
import json

url = 'http://localhost:8000'

'''def req(path, query, method, data={}):
    url = API_HOST + path
    print('HTTP Method: %s' % method)
    print('Request URL: %s' % url)
    print('Headers: %s' % headers)
    print('QueryString: %s' % query)

    if method == 'GET':
        return requests.get(url, headers = headers)
    else:
        return requests.post(url, headers=headers, data=data)

resp = req('', '', 'POST')'''

def start(user, problem, count):
    uri = url + '/start/' + user + '/' + str(problem) + '/' + str(count)
    req = requests.post(uri).json()
    return req
def oncall(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers = {'X-Auth-Token' : token}).json()

def action(token,cmd):
    uri = url + '/action'
    return requests.post(uri,headers={'X-Auth-Token': token},json = {'commands': cmd}).json()


user = 'tester'
problem = 0
count = 2

ret = start(user,problem,count)
print(ret['token'])
#print(oncall(ret['token']))
calls={}
start=[[] for i in range(5)]
end = [[] for i in range(5)]
elevators={}
oncall(ret['token'])
action(ret['token'],[{'elevator_id':0,'command':'UP'},{'elevator_id': 1, 'command': 'STOP'}])
oncall(ret['token'])
action(ret['token'],[{'elevator_id':0,'command':'UP'},{'elevator_id': 1, 'command': 'STOP'}])
oncall(ret['token'])
action(ret['token'],[{'elevator_id':0,'command':'UP'},{'elevator_id': 1, 'command': 'STOP'}])
oncall(ret['token'])
action(ret['token'],[{'elevator_id':0,'command':'UP'},{'elevator_id': 1, 'command': 'STOP'}])
oncall(ret['token'])
action(ret['token'],[{'elevator_id':0,'command':'UP'},{'elevator_id': 1, 'command': 'STOP'}])
tmp2 = oncall(ret['token'])
tmp = action(ret['token'],[{'elevator_id':0,'command':'UP'},{'elevator_id': 1, 'command': 'STOP'}])
tmp2 = oncall(ret['token'])
print('call state: ',tmp2['calls'])
print('ele state: ',tmp['elevators'])
print()
print()
for i in tmp2['calls']:
    start[i['start']-1].append(i['id'])
    end[i['end']-1].append(i['id'])

print('start: ', start)
print('end: ', end)
print('ele1: ', tmp['elevators'][0])
print('ele2: ', tmp['elevators'][1])
tmp = action(ret['token'],[{'elevator_id':0,'command':'STOP'},{'elevator_id': 1, 'command': 'OPEN'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'OPEN'},{'elevator_id':1,'command':'ENTER','call_ids':start[0]}])
print('ele1: ', tmp['elevators'][0])
print('ele2: ', tmp['elevators'][1])
tmp = action(ret['token'],[{'elevator_id':0,'command':'CLOSE'},{'elevator_id': 1, 'command': 'CLOSE'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'DOWN'},{'elevator_id': 1, 'command': 'UP'}])
print('ele1: ', tmp['elevators'][0])
print('ele2: ', tmp['elevators'][1])
tmp = action(ret['token'],[{'elevator_id':0,'command':'STOP'},{'elevator_id': 1, 'command': 'STOP'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'OPEN'},{'elevator_id': 1, 'command': 'OPEN'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'ENTER','call_ids': [0,1]},{'elevator_id': 1, 'command': 'EXIT','call_ids':[2,5]}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'CLOSE'},{'elevator_id': 1, 'command': 'CLOSE'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'DOWN'},{'elevator_id': 1, 'command': 'UP'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'STOP'},{'elevator_id': 1, 'command': 'UP'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'OPEN'},{'elevator_id': 1, 'command': 'STOP'}])
print('ele1: ', tmp['elevators'][0])
print('ele2: ', tmp['elevators'][1])
tmp = action(ret['token'],[{'elevator_id':0,'command':'EXIT','call_ids':[1]},{'elevator_id': 1, 'command': 'OPEN'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'CLOSE'},{'elevator_id': 1, 'command': 'EXIT','call_ids':[3]}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'DOWN'},{'elevator_id': 1, 'command': 'CLOSE'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'STOP'},{'elevator_id': 1, 'command': 'STOP'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'OPEN'},{'elevator_id': 1, 'command': 'STOP'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'ENTER','call_ids': [4]},{'elevator_id': 1, 'command': 'STOP'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'CLOSE'},{'elevator_id': 1, 'command': 'STOP'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'DOWN'},{'elevator_id': 1, 'command': 'STOP'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'STOP'},{'elevator_id': 1, 'command': 'STOP'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'OPEN'},{'elevator_id': 1, 'command': 'STOP'}])
tmp = action(ret['token'],[{'elevator_id':0,'command':'EXIT','call_ids':[0,4]},{'elevator_id': 1, 'command': 'STOP'}])

'''action(ret['token'],[{'elevator_id':0,'command':'UP'},{'elevator_id': 1, 'command': 'STOP'}])
print(oncall(ret['token']))
action(ret['token'],[{'elevator_id':0,'command':'UP'},{'elevator_id': 1, 'command': 'STOP'}])
print(oncall(ret['token']))
action(ret['token'],[{'elevator_id':0,'command':'UP'},{'elevator_id': 1, 'command': 'STOP'}])
print(oncall(ret['token']))
action(ret['token'],[{'elevator_id':0,'command':'UP'},{'elevator_id': 1, 'command': 'STOP'}])
print(oncall(ret['token']))'''
