from itertools import combinations

def solution(numbers):

    # 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아라
    answer = []

    for unit in list(combinations(numbers, 2)):
        x, y = unit
        sum = x + y
        if sum not in answer:
            answer.append(sum)

    answer = sorted(answer)

    return answer


print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))

