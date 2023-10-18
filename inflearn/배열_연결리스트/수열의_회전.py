# 정수 배열과 k 값이 주어졌을 떄, k 만큼 배열을 회전시킬 수 있도록 프로그래밍

# 자르는 기준을 정하는건 생각하기 나름이기 때문에 k 만큼 반복하도록 하면서 popleft() 사용하면 될 거라고 생각
# 1. queue 에 nums[i] 를 담는다.
# 2. k 만큼 반복하며 queue 의 원소를 popleft() 해서 맨 뒤에 넣는다.
# 3. queue 를 list 로 변환하고, 반환한다.

from collections import deque

def solution(nums, k):
    queue = deque(nums) # 1

    for i in range(k): # 2
        queue.append(queue.popleft())

    answer = list(queue) # 3
    return answer


print(solution([3, 7, 1, 5, 9, 2, 8], 3))
print(solution([2, 12, 2, 1, 3, 3, 9], 2))
print(solution([1, 2, 5, 4, 6, 7, 9], 6))
print(solution([1, 3, 6, 8, 14, 2, 1, 7], 5))
