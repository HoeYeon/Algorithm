# 보석진열대 문제

# 슬라이딩윈도우로 풀기


def solution(gems):
    answer = []

    # gems의 종류 계산  O(n)
    gem_kind = []
    for gem in gems:
        if gem not in gem_kind:
            gem_kind.append(gem)
    print(gem_kind)

    dist = len(gem_kind)

    # 브루트포스 O(n^3)
    for gap in range(dist, len(gems) + 1):  # gap을 늘려가며 진열대 확인
        for start in range(0, len(gems) - gap + 1):  # 시작 지점
            dict = {}  # 딕셔너리 생성
            for kind in gem_kind:
                dict[kind] = 'false'

            for end in range(0, gap):  # 끝 지점
                dict[gems[start + end]] = "true"  # 해당 gem이 존재한다
                print(gems[start + end], end=' ')
            print()
            print("dict : ", list(dict.values()))

            if "false" not in list(dict.values()):  # 모든 gem이 존재한다면
                answer.append([start + 1, start + gap])  # answer에 삽입
                print(start + 1, start + gap)  # 해당 start, end좌표 출력

        if len(answer) > 0:  # 답이 하나라도 있으면 break/ 최소구간을 이미 만족
            break
        print("gap++")
        # print(dict)
    # for gem in gems:
    #     if gem in gem_kind:

    return answer[0]  # 최소구간 답중 첫번째 인자가 start가 가장 작은 답
