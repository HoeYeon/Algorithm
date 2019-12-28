mat = [[1,1],[1,0]]
def mul(A,B):
    C = [[0,0],[0,0]]
    C[0][0] = (A[0][0]*B[0][0] + A[0][1]*B[1][0])%1000000
    C[0][1] = (A[0][0]*B[0][1] + A[0][1]*B[1][1])%1000000
    C[1][0] = (A[1][0]*B[0][0] + A[1][1]*B[1][0])%1000000
    C[1][1] = (A[1][0]*B[0][1] + A[1][1]*B[1][1])%1000000
    return C

def fib(A,n):
    if n>1:
        A = fib(A,n//2)
        A = mul(A,A)
        if n&1:
            A = mul(A,mat)
    return A

N = int(input())
result = fib(mat,N-1)
if N ==0:
    result[1][0] = 0
print((result[1][0]%1000000+result[1][1]%1000000)%1000000)