from operator import itemgetter

def solution(n, stages):
  answer = []
  fails = []
  stop_count = [0] * (n + 2) # 0번 인덱스는 안쓰고 n + 1 인덱스까지 필요하니까 n + 2 로 길이 설정
  every_challenger_count = len(stages)

  for i in stages:
    stop_count[i] += 1

  for i in range(1, n + 1):
    # 실패율 = 현재 스테이지를 통과하지 못한 인원 / 도전 인원
    cur_failed_count = stop_count[i]
    cur_challenger_count = every_challenger_count

    if every_challenger_count == 0:
      fails.append((i, 0)) # 스테이지에 도달한 유저가 없는 경우 실패율 0으로 처리

    else:
      fails.append((i, cur_failed_count / cur_challenger_count))
      every_challenger_count -= stop_count[i]

  fails.sort(key=itemgetter(1), reverse=True)

  for i in range(len(fails)):
    answer.append(fails[i][0])

  return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(5, [3, 3, 3, 3]))