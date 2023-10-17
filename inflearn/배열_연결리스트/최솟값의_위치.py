# 매개변수 nums 에 길이가 n 인 수열이 주어지면, 수열의 원소 중에서 가장 작은 값을 찾아
    # 그 값의 nums 배열의 인덱스 번호를 반환하는 프로그램 작성

# 1. 처음 원소 값을 기억한다. (값과 인덱스 주소)
# 2. 처음 원소부터 끝 원소까지 확인해야한다.
# 3. 다음 원소 값과 처음 원소 값을 비교한다.
    # 다음 원소 값이 더 크다면 기억을 유지한다.
    # 다음 원소 값이 더 작다면 기억(값, 인덱스 주소)을 변환한다.
# 4. 끝 원소까지 확인이 끝났다면, 기억의 인덱스 주소 값을 출력한다.

# 6. 프로그램 코드 작성
def solution(nums):
    memory = (nums[0], 0) # 1
    for next_address, next_num in enumerate(nums): # 2
        if next_num < memory[0]: # 3
            memory = (next_num, next_address)

    return memory[1]


# 모든 테스트 케이스 확인
nums1 = [7, 10, 5, 3, 2, 15, 19]
nums2 = [-12, 12, 30, -15, -5, 3, 9, -11, 14]
nums3 = [17, 11, 5, 8, 23, 29, 19, 12, 25, 16, 2]
nums4 = [7, 5, 12, -9, -12, 22, -30, -35, -21]

print(solution(nums1))
print(solution(nums2))
print(solution(nums3))
print(solution(nums4))
