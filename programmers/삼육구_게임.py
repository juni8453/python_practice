# def solution(number):
#   my_list = list(str(number))
#   count3 = my_list.count(str(3))
#   count6 = my_list.count(str(6))
#   count9 = my_list.count(str(9))
#
#   return count3 + count6 + count9

def solution(order):
  # 한 줄 코드
  # answer = len([1(아무거나) for ch in str(order) if ch in '369'])
  answer = 0

  for ch in str(order):
    if ch in '369':
      answer += 1

  return answer

print(solution(29423))