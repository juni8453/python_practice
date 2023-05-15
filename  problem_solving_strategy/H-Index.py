def solution(citations):
    # n 개의 논문 중 h 번 이상 인용된 논문이 h 개 이상, 나머지 논문이 h 번 이하로 인용되었다면 해당 h 가 H-Index 이다.
    # [0, 1, 4, 5, 6, 7]
    # 0번 이상 인용된 논문 갯수 = 6개 -> 전체 길이 - index
    # 1번 이상 인용된 논문 갯수 = 5개
    # 4번 이상 인용된 논문 갯수 = 4개
    # -------
    # 5번 이상 인용된 논문 갯수 = 3개
    # 오름차순을 했기 때문에 현재 논문 인용 횟수 기준 앞 쪽은 무조건 현재 논문 인용 횟수보다 적게 인용되는거라 나머지 논문의 인용 횟수는 신경쓰지 않아도 된다.
    citations.sort()

    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx: # 현재 논문의 인용 횟수가
            return len(citations) - idx

print(solution([4, 0, 6, 1, 5, 7]))