def solution(my_string):
  answer = ''
  my_dict = dict()

  for s in my_string:
    my_dict[s] = True

  for d in my_dict:
    answer += d

  return answer

print(solution("people"))
print(solution("We are the world"))