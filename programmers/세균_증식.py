def solution(n, t):
  answer = 1

  # 결과 값 * 2 를 t 만큼 반복하는 것.
  for _ in range(t):
    answer *= 2

  return answer