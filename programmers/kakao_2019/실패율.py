from operator import itemgetter

def solution(n, stages):
  my_tuple = []
  stop_count = [0] * (n + 2) # 0번 인덱스는 안쓰고 n + 1 인덱스까지 필요하니까 n + 2 로 길이 설정
  every_challenger_count = len(stages)

  for i in stages:
    stop_count[i] += 1

  for i in range(1, n + 1):
    # 실패율 = 현재 스테이지를 통과하지 못한 인원 / 도전 인원
    cur_failed_count = stop_count[i]
    cur_challenger_count = every_challenger_count

    if every_challenger_count == 0:
      my_tuple.append((0, i)) # 스테이지에 도달한 유저가 없는 경우 실패율 0으로 처리
      continue

    failed_percent = cur_failed_count / cur_challenger_count
    my_tuple.append((failed_percent, i))
    every_challenger_count -= stop_count[i]

  my_tuple.sort(key=itemgetter(0), reverse=True)

  sub_list = []
  for i in range(len(my_tuple)):
    sub_list.append(my_tuple[i][1])

  return sub_list

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(5, [3, 3, 3, 3]))


# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.