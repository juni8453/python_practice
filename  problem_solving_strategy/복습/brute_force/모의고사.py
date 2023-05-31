def solution(answers):
    result = []
    scores = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if [1,2,3,4,5][idx % 5] == answer:
            scores[0] += 1

        if [2,1,2,3,2,4,2,5][idx % 8] == answer:
            scores[1] += 1

        if [3,3,1,1,2,2,4,4,5,5][idx % 10] == answer:
            scores[2] += 1

    # 이렇게 하면, 점수가 가장 높은 학생의 순번을 오름차순으로 넣을 수 있고,
    # 점수가 동일한 학생이더라도 오름차순으로 넣을 수 있다.
    max_score = max(scores)
    for idx, score in enumerate(scores):
        if max_score == score:
            result.append(idx + 1)

    return result


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
