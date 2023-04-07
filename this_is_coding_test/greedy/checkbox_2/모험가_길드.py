def solution(n, people):
  cur_people = 0
  group = 0

  for fear in people:
    cur_people += 1
    if cur_people >= fear:
      group += 1
      cur_people = 0

  return group

print(solution(n=5, people=[2,3,1,2,2]))