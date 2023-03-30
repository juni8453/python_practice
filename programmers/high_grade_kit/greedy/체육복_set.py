def solution(n, lost, reserve):
  # reserve 에서도 도난을 당할 수 있다. 즉, lost 와 reserve 의 중복이 발생할 수 있음
  # 따라서 set() 사용
  reserve_set = set(reserve) - set(lost)
  lost_set = set(lost) - set(reserve)

  for reserve in reserve_set:
    reserve_front = reserve - 1
    reserve_back = reserve + 1

    if reserve_front in lost_set:
      lost_set.remove(reserve_front)

    elif reserve_back in lost_set:
      lost_set.remove(reserve_back)

  return n - len(lost_set)

print(solution(5, [2,4], [1,3,5]))