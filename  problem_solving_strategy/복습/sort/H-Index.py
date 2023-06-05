def solution(citations):
    # [0,1,3,5,6]
    # h번 (1번) 이상 인용된 논문 4편 >= h편 (1편) 이상
    # h번 (2번) 이상 인용된 논문 3편 >= h편 (2편) 이상
    # h번 (3번) 이상 인용된 논문 3편 >= h편 (3편) 이상
    # h번 (4번) 이상 인용된 논문 2편 <= h편 (4편) 이상
    # -> 즉 해당 연구자 최대 h-index 는 3

    # 과학자의 H-Index 를 반환하는 함수를 구현해라.

    citations = sorted(citations)
    print(citations)

    # [0, 1, 3, 5, 6]
    # 만약에 h 기준이 1이라고 하면, 1번 이상 인용된 논문이 1개 이상인지? 확인하면 된다.
    # 오름차순을 했으니까 index 를 구해서 전체 리스트 길이에서 1 이 존재하는 index 길이를 빼면 그 뒤에는 어짜피
    # 전부 1 이상이기 때문에 1개 이상인지 확인할 수 있다.
    for idx, citation in enumerate(citations):
        print('위치:', idx)
        print('현재 위치의 citation:', citation)
        print('현재 위치의 citations 만큼 인용된 논문의 수는?:', len(citations) - idx)
        if citation >= len(citations) - idx:
            return len(citations) - idx

print(solution([3,0,6,1,5]))