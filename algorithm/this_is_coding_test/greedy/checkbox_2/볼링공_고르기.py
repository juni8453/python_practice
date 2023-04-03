def solution(n, m, data):
  answer = 0
  count_sum = 0

  # 무게 순으로 리스트 초기화
  ball_weight = [0] * (m + 1)
  for i in data:
    ball_weight[i] += 1

  for i in ball_weight:
    count_sum += ball_weight[i]

  for i in range(1, len(ball_weight)):
    answer += ball_weight[i] * (count_sum - ball_weight[i])
    count_sum -= ball_weight[i]

  return answer

print(solution(5, 3, [1, 3, 2, 3, 2]))
print(solution(8, 5, [1, 5, 4, 3, 2, 4, 5, 2]))