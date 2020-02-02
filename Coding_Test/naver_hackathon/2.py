# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    ## 홀수 +1
    thr = len(S)//2 if len(S)%2 ==0 else len(S)//2 +1
    start = 0
    end = len(S) -1
    S = list(S)
    for i in range(thr):
        if S[start+i] == '?' and S[end-i] == '?':
                S[start+i] = S[end-i] = 'a'
        elif S[start+i] != S[end-i]:
            if S[start+i] == '?':
                S[start+i] = S[end-i]
            elif S[end-i] == '?':
                S[end-i] = S[start+i]
            else:
                return 'NO'
    S = ''.join(S)
    return S
