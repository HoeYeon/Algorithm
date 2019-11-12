for i in range(int(input())):
    A,B = input().split(' ')
    c = A.count(B)
    print('#'+str(i+1),len(A) - c*len(B) + c)
