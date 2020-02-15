words =['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
n = 3

def solution1(n,words):
    word_dict = {}
    check = False
    for i in range(len(words)):
        if i != 0 and words[i-1][-1] != words[i][0]:
            check = True
            break
        try:
            word_dict[words[i]] += 1
        except:
            word_dict[words[i]] = 1
            continue
        check = True
        break
    num = i%n
    seq = i//n
    print(num+1,seq+1)
    return([num+1,seq+1] if check else [0,0])


def solution2(n,words):
    word_dict = {}
    check = False
    for i in range(len(words)):
        if i != 0 and (words[i-1][-1] != words[i][0] or words[i] in word_dict):
            check = True
            break
        word_dict[words[i]] = 1
    return [i%n+1,i//n+1] if check else [0,0]
    
solution1(n,words)
        