from operator import itemgetter

def solution(food_times, k):
  answer = -1
  foods = []
  n = len(food_times)
  for i in range(n):
    foods.append((food_times[i], i + 1))

  foods.sort() # [(1,2), (2,3), (3,1)] (먹는데 걸리는 시간, 먹는 음식 순서)

  pretime = 0

  # i : 튜플 자체 인덱스, food : 튜플
  for i, food in enumerate(foods):
    diff = food[0] - pretime
    if diff != 0:
      spend = diff * n

      if spend <= k: # 남은 시간이 더 많다면 뺄 수 있음.
        k -= spend
        pretime = food[0] # 현재 시간으로 이전 시간을 갱신
      else: # 남은 시간이 필요 시간보다 더 적다면 뺄 수 없음.
        k %= n
        sublist = sorted(foods[i:], key=itemgetter(1)) # 남은 음식의 food[0] 기준으로
        return sublist[k][1] # 남은 음식의 번호 반환
    n -= 1
  return answer

print(solution(food_times=[3,1,2], k=5))