import sys
input = sys.stdin.readline
li = []
for i in range(int(input())):
    a,b = input().split()
    li.append([int(a),b])
print('\n'.join([str(i[0])+' '+i[1] for i in sorted(li,key = lambda x: x[0])]))
