from math import ceil


def solution(n):
    wordCount = 9
    wordLen = 1
    while n > wordCount * wordLen:
        n -= wordCount*wordLen
        wordCount *= 10
        wordLen += 1
    wordNum = ceil(n / wordLen)
    remain = n % wordLen
    targetWord = (wordCount // 9) + (wordNum-1)

    return int(str(targetWord)[remain-1])
