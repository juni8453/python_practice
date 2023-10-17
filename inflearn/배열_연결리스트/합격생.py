# k(커트라인) 이상의 점수를 받은 응시자가 몇 명인지 구해내는 프로그램

# 1. 응시자 수만큼 확인해야한다.
# 2. 현재 응시자의 점수와 k 를 비교한다.
    # score[i] >= k 라면, 응시자 수를 추가한다.
# 3. 응시자 수를 반환한다.

def solution(scores, k):
    answer = 0

    for cur_score in scores: #1
        if cur_score >= k:
            answer += 1

    return answer


scores1 = [60, 50, 80, 90, 55, 70, 65, 43]
scores2 = [10, 20, 30, 40, 50]
scores3 = [50, 65, 75, 87, 90, 55, 78, 93, 100]
scores4 = [99, 30, 50, 55, 68, 70, 90, 100]
k1 = 60
k2 = 60
k3 = 70
k4 = 80
print(solution(scores1, k1))
print(solution(scores2, k2))
print(solution(scores3, k3))
print(solution(scores4, k4))