# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    a = bin(A)[2:]
    b = bin(B)[2:]
    zero_count = 0
    ans = '0'
    for i in range(len(b)-1,-1,-1):
        after =''
        if b[i] == '1':
            after += a
            after += '0'*zero_count
            zero_count +=1
        else:
            zero_count +=1
            continue
        print(ans,after)
        carry = False
        result = ''
        idx = len(after)-1
        for j in range(len(ans)-1,-1,-1):
            print('we add :',ans[j],after[idx])
            tmp = int(ans[j]) + int(after[idx])
            if carry:
                tmp += 1
            if tmp >= 2:
                carry = True
                tmp -= 2
            else:
                carry = False
            result = str(tmp) + result
            print('adding result1: ',result)
            idx -= 1
        
        if carry:
            if after[idx] == '1':
                result = '01' + result
            else:
                result = '1' + result
        result = after[:idx] + result
        print('result: ',result)
        ans = result
        print('ans: ',ans)
        zero_count += 1
    return(sum(list(map(int,ans))))

if __name__ == "__main__":
    print(solution(3,7))