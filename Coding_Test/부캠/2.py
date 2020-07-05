def makeSet(arr):
    arr.sort()
    array_set = [arr[i] for i in range(1, len(arr)) if arr[i - 1] != arr[i]]
    array_set.append(arr[0])
    return array_set


def setSum(base, other):
    return makeSet([*base, *other])


def setComplement(base, other):
    return [elem for elem in base if elem not in other]


def setIntersect(base, other):
    return [elem for elem in base if elem in other]


def solution(arrayA, arrayB):
    A = makeSet(arrayA)
    B = makeSet(arrayB)
    return [
        len(A),
        len(B),
        len(setSum(A, B)),
        len(setComplement(A, B)),
        len(setIntersect(A, B)),
    ]

