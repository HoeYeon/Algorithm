# 핸드폰 자판 문제


def solution(numbers, hand):
    answer = ""
    left_zone = [1, 4, 7, 10]
    right_zone = [3, 6, 9, 12]
    left_hand = 10  # 왼손의 위치
    right_hand = 12  # 오른손의 위치
    number = -1

    for num in numbers:
        if num == 0:
            number = 11
        else:
            number = num
        # print(number)
        # print("hand place :" ,left_hand, right_hand)
        if number in left_zone:
            answer += 'L'
            left_hand = number
        elif number in right_zone:
            answer += 'R'
            right_hand = number

        else:
            # todo  거리비교하기
            left_temp = left_hand
            right_temp = right_hand
            left_dist = 0
            right_dist = 0
            if left_temp in left_zone:
                left_temp += 1
                left_dist += 1
            if right_temp in right_zone:
                right_temp -= 1
                right_dist += 1

            # print(answer)
            # print("distance :",abs(number - left_temp)//3 , left_dist, abs(number - right_temp)//3 , right_dist )
            if abs(number - left_temp) // 3 + left_dist < abs(number - right_temp) // 3 + right_dist:
                answer += 'L'
                left_hand = number
            elif abs(number - left_temp) // 3 + left_dist == abs(number - right_temp) // 3 + right_dist:
                if hand == "left":
                    answer += 'L'
                    left_hand = number
                else:
                    answer += 'R'
                    right_hand = number
            elif abs(number - left_temp) // 3 + left_dist > abs(number - right_temp) // 3 + right_dist:
                answer += 'R'
                right_hand = number

    return answer
