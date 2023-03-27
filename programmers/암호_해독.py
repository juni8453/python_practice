def solution(cipher, code):
  answer = cipher[code - 1 :: code]
  return answer

print(solution(cipher="dfjardstddetckdaccccdegk", code=4))