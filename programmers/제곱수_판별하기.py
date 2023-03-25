import math

def solution(n):
  number = int(math.sqrt(n))

  if number * number != n or number == 1:
    return 2

  return 1

print(solution(976))
print(solution(144))
print(solution(1))