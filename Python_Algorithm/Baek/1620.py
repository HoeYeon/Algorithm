import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pkmn = [] 
pkmn_dic = {} 
 
for i in range(n) :    
    pk = input()[:-1]
    pkmn.append(pk)
    pkmn_dic[pk] = i + 1
 
re =''
for _ in range(m): 
    query = input()[:-1]
    re += pkmn[int(query)-1] + '\n' if query.isdigit() else str(pkmn_dic[query]) + '\n'
print(re)