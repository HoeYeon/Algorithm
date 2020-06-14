## 한 단어가 다른 단어에 포함된 문자열인지?


def isSubstring(S1, S2):
    S1 = S1 + S1
    for i in range(len(S1)):
        check = True
        for j in range(len(S2)):
            if S1[i + j] != S2[j]:
                check = False
                break
        if check:
            return True
    return False


if __name__ == "__main__":
    S1, S2 = input().split()
    print(isSubstring(S1, S2))
