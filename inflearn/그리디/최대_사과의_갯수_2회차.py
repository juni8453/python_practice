def solution(box, limit):
    answer = 0

    box = sorted(box, key=lambda x: x[1], reverse=True)

    for i in range(len(box)):
        b_count = box[i][0]
        b_wight = box[i][1]

        if limit >= b_count:
            answer += (b_count * b_wight)
            print(f'answer = {answer}')
            limit -= b_count

        elif limit <= b_count:
            print(f'b_wight = {b_wight}')
            answer += (limit * b_wight)
            break

    return answer


print(solution([
    [2, 20], [2, 10], [3, 15], [2, 30]
], 5))

print(solution([
    [1, 50], [2, 20], [3, 30], [2, 31], [5, 25]
], 10))

print(solution(
    [[3, 40], [5, 20], [5, 70], [1, 80], [5, 30], [3, 35]
], 15))