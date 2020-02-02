# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import permutations
def solution(A):
    B = [j for j in A if len(j)==len(set(j))]
    C = []
    for i in range(len(B)):
        C.extend(list(map(''.join, permutations(B,i+1))))
    D = [len(j) for j in C if len(j)==len(set(j))]
    return max(D) if len(D) != 0 else 0
