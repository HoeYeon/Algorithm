mat = [[1,1],[1,0]]
def mul(A,B):
    C = [[0,0],[0,0]]
    C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
    C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
    C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]
    C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1]
    return C

def fib(A,n):
    if n>1:
        A = fib(A,n//2)
        A = mul(A,A)
        if n&1:
            A = mul(A,mat)
    return A

N = int(input())
result = fib(mat,N)
if N ==0:
    result[0][1] =0
print(result[0][1])


'''import numpy as np
mat = np.array([[1,1,],[1,0]])

def fib(A,n):
    if n>1:
        A = fib(A,n//2)
        A = np.dot(A,A)
        if n&1:
            A = np.dot(A,mat)
    return A
N = int(input())
result = fib(mat,N) if N != 0 else [[0,0]]
print(result[0][1])'''
