dd = {
    "a": 20, 
    "d": 8, 
    "c": 7,  
    "b": 4, 
    "e": 28 } 

print(dict(sorted(dd.items())))
print(dict(sorted(dd.items(),key=lambda x: x[1])))

li = [5,2,3,7,1,4,8,9,10]
print(sorted(li))
print(sorted(li,reverse=True))

li = [[10,0],[0,0],[10,10],[0,10]]
print(sorted(li))
print(sorted(li,reverse=True))

li = [[10,0],[0,0],[10,10],[0,10]]
print(sorted(li,key=lambda x:x[1]))
print(sorted(li,reverse=True,key=lambda x:x[1]))