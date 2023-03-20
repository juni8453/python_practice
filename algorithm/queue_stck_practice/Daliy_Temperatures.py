def dailyTemperatures(temp):
  answer = [0] * len(temp)
  stack = []
  # index 와 원소를 동시 접근할 수 있게 하는 내장 함수 enumerate()
  # 기본적으로 인덱스와 원소로 이루어진 tuple 을 만들어준다.
  for cur_day, cur_temp in enumerate(temp):
    # stack 이 비지 않았고, stack 의 top 이 현재 온도보다 낮다면,
    while stack and stack[-1][1] < cur_temp:
      prev_day, _ = stack.pop()
      answer[prev_day] = cur_day - prev_day
    stack.append((cur_day, cur_temp))
  return answer

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))