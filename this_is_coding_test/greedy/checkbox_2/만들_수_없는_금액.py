def solution(n, data):
  data.sort()

  # 만들 수 없는 최소 값
  target = 1

  # 만들 수 없는 최소 값보다 동전이 작을 때
  for i in data:
    if target < i:
      break
    target += i

  return target

print(solution(n=5, data=[3,2,1,1,9]))