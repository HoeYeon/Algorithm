def solution(sticker):
    s = sticker
    if len(s) == 1:
        return s[0]
    elif len(s) == 2:
        return max(s[0],s[1])

    if len(s) < 3:
        return max(s)

    dp = [[0 for i in range(100000)] for j in range(2)]
    # 2번째를 뗐을 때
    dp[0][0] = 0
    dp[0][1] = s[1]
    ## 처음 스티커 뗐을때
    dp[1][0] = s[0]
    dp[1][1] = s[0]
    # 처음을 뗐을때는 마지막을 수행하면 안되니깐 2~n-2까지 수행
    
    for i in range(2):
        for j in range(2,len(s)-i):
            dp[i][j] = max(dp[i][j-2]+s[j], dp[i][j-1])
    '''for i in range(2,len(s)-1):
        dp[0][i] = max(dp[0][i-2]+s[i],dp[0][i-1])
    for i in range(2,len(s)):
        dp[1][i] = max(dp[1][i-2]+s[i], dp[1][i-1])'''

    answer = max(dp[0][len(s)-1],dp[1][len(s)-2])

    return answer
