# 0,1 로 이루어진 수열이 주어졌을 때 1이 가장 많이 연속된 길이를 반환하는 프로그램

# 1. 수열 길이만큼 반복해야한다,
# 2. 이전에 1이 몇 번 연속되었는지 저장하는 메모리가 필요하다.
# 3. 현재 원소가 0이라면,
    # 현재까지 연속된 count >= 직전에 연속된 memory 라면, memory = count
        # max() 쓰면 간단해짐.
    # count 초기화
    # '>=' 가 아니라 '>' 라면 같은 count == memory 인 경우에 count 초기화가 안되기 때문에.
        # max() 쓰면 간단해짐.
# 4. 현재 원소가 1이라면, count 1 증가
# 5. 0 이 비교 트리거로 사용되는데, 끝까지 0 이 안나오는 경우가 있을 수 있다.
    # for 가 끝나고 다시 하번 memory 와 count 비교

def solution(nums):
    memory = 0
    count = 0

    for num in nums:
        if num == 0:
            memory = max(memory, count)
            count = 0
        else:
            count += 1

    memory = max(memory, count)

    return memory


print(solution([1,1,0,1,1,1,0,1,1,1,1,1]))
print(solution([0,0,1,0,1,0,0]))
print(solution([1,1,1,1,1]))
print(solution([1,0,1,1,0,1,1,1,0,1,1,1,0,1]))