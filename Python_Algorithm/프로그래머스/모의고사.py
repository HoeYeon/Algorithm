supo = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
answers = [1,3,2,4,2]
def solution(answers):
    ans = [0,0,0]
    for i in range(len(answers)):
        for j in range(3):    
            if answers[i] == supo[j][i%len(supo[j])]:
                ans[j] += 1
    result = [i+1 for i, x in enumerate(map(lambda x :max(ans) == x,ans)) if x]
    return result
print(solution(answers))