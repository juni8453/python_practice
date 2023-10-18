# 1. 왼쪽에서 오른쪽으로 바라보면서 비교하기 위해 기둥을 순서를 뒤집는다.
# 2. 가장 왼쪽 기둥 높이를 저장한다. (memory_num)
# 3. 두 번째 기둥부터 비교한다. (next_num)
# memory_num < next_num 라면 count 증가 후 기준을 next_num 으로 변경
# memory_num >= next_num 라면 아무 동작 X
# 4. count + 1 한 뒤 출력

import sys

count = 0
n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.reverse() # 1
memory_num = nums[0] # 2

for i in range(1, len(nums)):
    next_num = nums[i] # 3

    if memory_num < next_num:
        count += 1
        memory_num = next_num

print(count + 1)
