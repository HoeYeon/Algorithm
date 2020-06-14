from collections import Counter

S1, S2 = map(list, input().split())

# 간단
def usingSort(S1, S2):
    return True if S1.sort() == S2.sort() else False


# 효율성
def countElement(S1, S2):
    return True if Counter(S1) == Counter(S2) else False


if __name__ == "__main__":
    print("Sort: ", usingSort(S1, S2))
    print("Counter: ", countElement(S1, S2))
