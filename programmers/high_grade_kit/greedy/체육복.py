def solution(n, lost, reserve):
  answer = 0
  students = [1 for _ in range(n + 2)]
  students[0] = 0
  students[-1] = 0

  for i in reserve:
    students[i] += 1

  for i in lost:
    students[i] -= 1

  for i in range(1, n + 1):
    if students[i] == 0:
      if students[i - 1] == 2:
        students[i - 1] -= 1
        students[i] += 1

      elif students[i + 1] == 2:
        students[i + 1] -= 1
        students[i] += 1

      else:
        continue

  for i in range(1, len(students)):
    if students[i] >= 1:
      answer += 1

  return answer

print(solution(3, [3], [1]))
print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))