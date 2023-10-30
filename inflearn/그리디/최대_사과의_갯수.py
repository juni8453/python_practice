def solution(box, limit):
    answer = 0
    box = sorted(box, key=lambda x: (x[1]), reverse=True)

    for i in range(len(box)):
        box_count = box[i][0]
        box_kg = box[i][1]

        if limit >= box_count:
            limit -= box_count
            answer += box_count * box_kg

        elif limit < box_count:
            answer += limit * box_kg
            break

        print(f'answer = {answer}')
        print(f'limit = {limit}')

    return answer


print(solution([
    [2, 20], [2, 10], [3, 15], [2, 30]
], 5))
print(solution([
    [1, 50], [2, 20], [3, 30], [2, 31], [5, 25]
], 10))
print(solution([
    [3, 40], [5, 20], [5, 70], [1, 80], [5, 30], [3, 35]
], 15))
print(solution([
    [2, 70], [5, 100], [3, 90], [1, 95]
], 8))
print(solution([
    [80, 20], [50, 10], [70, 15], [70, 30], [80, 70], [90, 88], [70, 75]
], 500))