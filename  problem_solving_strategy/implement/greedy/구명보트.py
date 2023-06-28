def solution(people, limit):
    people.sort()
    set_count = 0
    left, right = 0, len(people) - 1

    while left < right:
        # 둘을 짝지을 수 있는 경우
        if people[right] + people[left] <= limit:
            set_count += 1
            right -= 1
            left += 1

        # 둘을 짝지을 수 없는 경우
        else:
            right -= 1

    return len(people) - set_count


print(solution([70, 50, 80, 50], 100))

# 최초 stack 으로 풀이 시도했으나 무게가 가장 작은 사람 2명을 짝지어 보트를 태우는 게 최적의 해는 아니라고 판단
# 최대한 알뜰살뜰 limit 까지 가깝게 사람을 태워야하니 Two Pointer 사용