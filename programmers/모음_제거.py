def solution(my_string):
  answer = ''
  collction = ['a', 'e', 'i', 'o', 'u']

  for i in my_string:
    if i not in collction:
      answer += i

  return answer
print(solution("nice to meet you"))
