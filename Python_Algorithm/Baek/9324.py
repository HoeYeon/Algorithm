import sys

input = sys.stdin.readline
result = ""
for i in range(int(input())):
    check = True
    alpha = [0 for k in range(26)]
    sen = input()[:-1]
    j = 0
    while j < len(sen):
        alpha[ord(sen[j]) - 65] += 1
        if alpha[ord(sen[j]) - 65] == 3:
            if j == len(sen) - 1:
                check = False
                break
            if sen[j] != sen[j + 1]:
                check = False
                break
            else:
                alpha[ord(sen[j]) - 65] = 0
                j += 2
        else:
            j += 1
    result += "OK\n" if check else "FAKE\n"
print(result)
