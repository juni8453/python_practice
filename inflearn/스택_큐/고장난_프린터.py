from collections import deque

def solution(nums):
    answer = 0
    queue = deque()
    for num in nums:
        queue.append(num)

    while queue:
        if len(queue) >= 3:
            queue.popleft()
            queue.popleft()
            queue.append(queue.popleft())

        else: # 2개 또는 1개 남아있는 경우
            answer = queue.pop()
            break

    return answer


print(solution([3,1,4,5,2,6,7]))
print(solution([10,8,3,1,4,5,2,6,7,9]))
print(solution([10,8,3,11,12,1,4,5,2,6,7,9]))
print(solution([10,8,3,1,4,5,2,11,13,6,7,12,9,14]))
print(solution([1,8,6,10,4,7,2,5,3,9]))