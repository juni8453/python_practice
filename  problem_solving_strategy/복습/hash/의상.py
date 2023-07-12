def solution(clothes):
    answer = 1
    clothes_dict = dict()

    # dictionary key = name, value = part 로 저장
    for name, part in clothes:
        clothes_dict[part] = clothes_dict.get(part, 0) + 1

    for part_count in clothes_dict.values():
        answer *= (part_count + 1)

    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))