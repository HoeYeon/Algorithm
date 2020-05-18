def getIndex(val, phone):
    return [[index, row.index(val)] for index, row in enumerate(phone) if val in row][0]


def getDistance(a, b):
    return (abs(a[0]-b[0]) + abs(a[1]-b[1]))


def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left_num = [1, 4, 7]
    right_num = [3, 6, 9]

    for i in numbers:
        if i in left_num:
            left = i
            answer += 'L'
        elif i in right_num:
            right = i
            answer += 'R'
        else:
            idx = getIndex(i, phone)
            l_idx = getIndex(left, phone)
            r_idx = getIndex(right, phone)
            l_d = getDistance(idx, l_idx)
            r_d = getDistance(idx, r_idx)
            if r_d < l_d or (r_d == l_d and hand == 'right'):
                right = i
                answer += 'R'
            elif r_d > l_d or (r_d == l_d and hand == 'left'):
                left = i
                answer += 'L'

    return answer
