
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
tmp = list(set(queries))
d = {}
for i in tmp:
    question_len = i.count('?')
    count = 0
    q_len = len(i)

    for j in new_words:
        if q_len == len(j):
            check = True
            k =0
            while k < q_len:
                if i[k] == '?':
                    k += question_len
                    continue
                if i[k] !=j[k]:
                    check = False
                    break
                k += 1
            if check:
                count = count+1
    d[i] = count
for i in queries:
    result.append(d[i])
