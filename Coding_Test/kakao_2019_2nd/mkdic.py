import requests

keys = ['name','age','loc']
result = [[123,45,666],[124,31,2412]]
ans = [{b:result[i][a] for a,b in enumerate(keys)} for i in range(2)]

data = requests.post('http://localhost:5000/', json=ans)
print(data)
