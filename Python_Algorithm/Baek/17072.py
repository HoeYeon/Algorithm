def i_f(li):
    num = (2126*li[0] + 7152*li[1] + 722*li[2])
    if 0 <= num < 510000:
        return '#'
    elif 510000 <= num < 1020000:
        return 'o'
    elif 1020000 <= num < 1530000:
        return '+'
    elif 1530000 <= num < 2040000:
        return '-'
    elif 2040000 <= num:
        return '.'
n, m = map(int, input().split(' '))
pixel = [[] for i in range(n)]
result = [[] for i in range(n)]
for i in range(n):
    li = list(map(int, input().split(' ')))
    for j in range(m):
        pixel[i].append([li[3*j], li[3*j+1], li[3*j+2]])
for i in range(len(pixel)):
    result[i] = [i_f(j) for j in pixel[i]]
for i in result:
    print(''.join(i))
