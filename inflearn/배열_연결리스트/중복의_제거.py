# 오름차순 된 배열이 주어졌을 때, 중복된 원소를 제거해 유일 값을 가지게 하도록 하고 내림차순으로 변환시키는 프로그램 작성
# 1. 비어있는 리스트를 생성하고 nums[0] 삽입
# 2. 두 번쨰 원소와 비교를 위해 nums[0] 을 따로 기억해두는 변수 생성
# 3. 두 번째 원소부터 반복해 기억하고 있는 memory 값과 현재 cur_num 값을 비교
# 4. 값이 다르다면 유일 값이라는 뜻이므로 삽입한 뒤 memory 값을 cur_num 으로 교체
# 5. 배열 거꾸로 회전한 뒤 반환


def solution(nums):
    answer = [nums[0]] # 1
    memory = nums[0] # 2

    for i in range(1, len(nums)):
        cur_num = nums[i]

        if memory != cur_num: # 3, 4
            answer.append(cur_num)
            memory = cur_num

    answer.reverse() # 5
    return answer


print(solution([0, 1, 1, 1, 2, 2, 2, 3]))
print(solution([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]))
print(solution([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))
print(solution([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))
