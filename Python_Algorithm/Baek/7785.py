import sys
input = sys.stdin.readline
d = {}
for i in range(int(input())):
    a,b = input().split()
    try:
        del d[a]
    except:
        d[a] = b
print('\n'.join(sorted(list(d.keys()),reverse=True)))