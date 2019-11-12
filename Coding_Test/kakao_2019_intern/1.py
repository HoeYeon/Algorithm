def solution(board, moves):
    answer = 0
    s = [[] for i in range(len(board[0]))]
    ba = []
    for i in range(len(board)-1,-1,-1):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                s[j].append(board[i][j])
    for i in range(len(moves)):
        if len(s[moves[i]-1]) != 0:
            ba.append(s[moves[i]-1].pop())
        if len(ba) > 1 and ba[-1] == ba[-2]:
            ba.pop()
            ba.pop()
            answer += 2
    return answer
