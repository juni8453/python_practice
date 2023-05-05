def solution(answers):
    # 1, 2, 3 수포자 정답이 다 같이 비교되야 한다.
    # 그러기 위해선 각 수포자 정답의 규칙을 찾아서 리스트를 만들어줘야 할듯
    # 1번 수포자는 1,2,3,4,5 (5개 기준)
    # 2번 수포자는 2,1,2,3,2,4,2,5 (8개 기준)
    # 3번 수포자는 3,3,1,1,2,2,4,4,5,5 (10개 기준)
    fir = [1, 2, 3, 4, 5]
    sec = [2, 1, 2, 3, 2, 4, 2, 5]
    th = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 수포자가 정답을 맞춘 개수
    answer_count = [0, 0, 0]

    # 정답을 담은 answers 리스트가 들어오면, 먼저 answer 부터 비교하도록
    for i in range(len(answers)):
        now_answer = answers[i]

        # 문제가 각 수포자의 찍는 기준 갯수보다 많이 나올 수 있으니까
        # 1번 수포자 기준 5로 나눈 나머지 인덱스를 비교하면 될 듯
        # 1번 수포자 확인
        if now_answer == fir[i % len(fir)]:
            answer_count[0] += 1

        # 2번 수포자 확인
        if now_answer == sec[i % len(sec)]:
            answer_count[1] += 1

        # 3번 수포자 확인
        if now_answer == th[i % len(th)]:
            answer_count[2] += 1

            # 가장 많은 문제를 맞힌 사람을 배열에 담는다.
    answer_list = []
    for idx, count in enumerate(answer_count):
        max_score = max(answer_count)

        # 해당 수포자가 맞춘 점수와 현재 최고 점수가 같다면,
        if count == max_score:
            answer_list.append(idx + 1)

    return answer_list

# 시험 문제가 10^4 로 주어지므로 O(n^2) 미만 알고리즘 작성
