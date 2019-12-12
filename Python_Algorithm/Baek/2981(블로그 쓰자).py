#https://suri78.tistory.com/37

import sys
import math
""" input """
N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
nums.sort()
""" find divisors """
mog = nums[-1] - nums[0]
divisor = [mog]
for i in range(2, int(math.sqrt(mog)) + 1):
    if mog % i == 0:
        divisor.append(i)
        divisor.append(mog//i)
divisor = list(set(divisor))
divisor.sort()
""" get answer """
for d in divisor:
    for i in range(N):
        if i == N - 1:
            print(d, end = " ")
        elif nums[i] % d != nums[i + 1] % d:
            break
