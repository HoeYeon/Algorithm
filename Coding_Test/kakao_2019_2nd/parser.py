import requests
import json

API_HOST = 'https://swapi.co/api/people/'

def req(path, query, method, data={}):
    url = API_HOST + path
    print('HTTP Method: %s' % method)
    print('Request URL: %s' % url)
    #print('Headers: %s' % headers)
    print('QueryString: %s' % query)

    if method == 'GET':
        return requests.get(url)
    else:
        return requests.post(url)

resp = req('', '', 'GET')
a = resp.json()['results']
for i in a:
    print(i.keys())
#print(resp.json()['results'])
'''def start(user, problem, count):
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
'''
