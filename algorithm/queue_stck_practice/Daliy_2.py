def dailyTemperatures(temp):
  answer = [0] * len(temp) # temp 길이만큼 0 원소로 answer list 초기화
  stack = []

  # O(n) 을 위해 한 번의 반복문으로 끝낸다.
  for cur_day, cur_temp in enumerate(temp):
    # stack 이 비지 않았거나, 가장 뒤 tuple 의 원소(Top) 의 온도보다 현재 온도가 낮다면 ?
    while stack and stack[-1][1] < cur_temp:
      prev_day, _ = stack.pop()
      answer[prev_day] = cur_day - prev_day
    stack.append((cur_day, cur_temp))
  return answer

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))