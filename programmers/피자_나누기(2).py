def solution(n):
  i = 1

  while(1):
    if (6 * i) % n == 0:
      return i
    i += i


print(solution(10))
print(solution(4))

print(solution(1))
print(solution(2))
print(solution(3))