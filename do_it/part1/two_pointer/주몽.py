import sys

answer = 0
n = int(sys.stdin.readline()) # 재료의 개수
m = int(sys.stdin.readline()) # 갑옷을 만드는데 필요한 수
nums = list(map(int, sys.stdin.readline().split())) # 재료 번호

# 오름차순 정렬 후 풀이 가능할 듯
nums.sort()

sp = 0
ep = len(nums) - 1

while sp < ep:
    if nums[sp] + nums[ep] > m:
        ep -= 1

    elif nums[sp] + nums[ep] < m:
        sp += 1

    elif nums[sp] + nums[ep] == m:
        answer += 1
        sp += 1
        ep -= 1

print(answer)


# 두 개의 재료를 합친 수 == m 이라면 갑옷 제작 가능
# n = 6, m = 9, nums = [2 7 4 1 5 3]

# 2 + 7 == 9 (경우의 수 1개)
# 4 + 5 == 9
# 총 2가지 경우의 수로 제작 가능능

# sorted_nums = [1 2 3 4 5 7]

