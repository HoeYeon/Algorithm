# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def flip( ch): 
    return '1' if (ch == '0') else '0'

def compareFlip(str, expected): 
  
    flipCount = 0
    for i in range(len( str)): 
        if (str[i] != expected): 
            flipCount += 1
        expected = flip(expected) 
    return flipCount 

def minFlip(str): 
    return min(compareFlip(str, '0'), 
            compareFlip(str, '1')) 
def solution(A):
    A = ''.join(map(str,A))
    return minFlip(A)
