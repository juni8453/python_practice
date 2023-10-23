# 정수 배열에서 두 개의 원소 합이 target 값과 같은 원소를 찾아 반환하는 프로그램
# 10,000 까지라 O(n^2) 시간 복잡도는 애매할 수 있다. 따라서 투포인터 사용
# 1. 가장 작은 수와 가장 큰 수 한 쌍부터 더하도록 하기 위해 오름차순
# 2. 가장 작은 수부터 커지는 left, 가장 큰 수부터 작아지는 right 변수를 할당
# 3. 더해서 같다면 정답 -> answer 리스트에 각 쌍을 삽입한 뒤 반환
# 4. 더해서 크다면 right 감소
# 5. 더해서 작다면 left 증가
# 6. target 과 같은 경우가 없다면 [0, 0] 반환

def solution(nums, target):
    answer = []
    nums.sort() # 1

    left_p = 0 # 2
    right_p = len(nums) - 1

    for _ in range(len(nums)):
        if left_p == right_p:
            return [0, 0]

        sum_left_right = nums[left_p] + nums[right_p]

        if sum_left_right == target: # 3
            answer.append(nums[left_p])
            answer.append(nums[right_p])
            return answer

        elif sum_left_right > target: # 4
            right_p -= 1

        elif sum_left_right < target: # 5
            left_p += 1

    return [0, 0] # 6


print(solution([7, 3, 2, 13, 9, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))