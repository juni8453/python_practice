def solution(weights, limit):
    answer = 0
    weights.sort()

    memory_kg = 0
    for kg in weights:
        memory_kg += kg
        if memory_kg <= limit:
            answer += 1

        else:
            break

    return answer


print(solution([300, 100, 230, 120, 90, 150, 60], 700))
print(solution([50, 90, 70, 120, 300, 200, 150, 180, 190], 1000))
print(solution([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200], 800))
print(solution([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140, 170], 1000))
print(solution([100, 110, 50, 50, 60, 70, 50, 55, 57],350))