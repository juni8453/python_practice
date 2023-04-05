from operator import itemgetter

def solution(food_times, k):
  # 더 이상 먹을 음식이 없을 때 -1 반환할 수 있도록.
  answer = -1

  # tuple, 정렬 사용
  foods = []
  n = len(food_times)
  for i in range(n):
    foods.append((food_times[i], i+1))

  # 먹는데 걸리는 시간 순으로 음식의 순서가 정렬된다.
  foods.sort()

  pretime = 0
  for i, food in enumerate(foods):
    diff = food[0] - pretime
    spend = diff * n
    if k >= spend:
      k -= spend
      pretime = food[0]
    else:
      k %= n
      sub_list = foods[i:] # 남은 음식 tuple 을 sub_list 에 차례대로 저장
      sorted(sub_list, key=itemgetter(1)) # 음식 순번으로 다시 정렬
      return sub_list[k][1]
    n -= 1 # for 문이 한 번 돌 때마다 하나의 음식이 클리어 됐으므로 -1

  return answer

print(solution(food_times=[3,1,2], k=5))