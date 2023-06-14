def solution(clothes):
    clothes_dict = dict()

    for name, category in clothes:
        clothes_dict[category] = clothes_dict.get(category, 0) + 1

    answer = 1
    for category in clothes_dict:
        answer *= (clothes_dict[category] + 1)

    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
                ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"],
                ["smoky_makeup", "face"]]))
