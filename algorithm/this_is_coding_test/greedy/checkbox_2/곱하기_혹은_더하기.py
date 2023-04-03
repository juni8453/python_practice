def solution(input):
  answer = 0

  for i in input:
    if int(i) <= 1 or answer <= 1:
      answer += int(i)

    else:
      answer *= int(i)

  return answer

print(solution(input='02984'))
print(solution(input='567'))
print(solution(input='110'))