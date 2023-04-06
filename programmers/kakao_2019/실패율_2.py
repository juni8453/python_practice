from operator import itemgetter

def solution(n, stages):
  answer = []
  fails = []
  total_user = len(stages)
  stop_user = [0 for _ in range(n + 2)]

  for i in stages:
    stop_user[i] += 1

  # 총 스테이지 개수만큼 순회
  for i in range(1, n + 1):
    # 현재 스테이지까지 도달한 인원이 없다면 실패율 0 으로 정의
    if stop_user[i] == 0:
      fails.append((i, 0))
    else:
      fails.append((i, stop_user[i] / total_user))
      total_user -= stop_user[i]

  fails.sort(key=itemgetter(1), reverse=True)

  for i in range(len(fails)):
    answer.append(fails[i][0])

  return answer

print(solution(5, [2,1,2,6,2,4,3,3]))