def solution(brown, yellow):
    sum_tile_count = brown + yellow

    for h_len in range(3, sum_tile_count):
        # 가로 >= 세로
        w_len = sum_tile_count // h_len

        # 전체 넓이를 세로 길이로 나눴을 때 나머지가 존재하면 안됨
        if sum_tile_count % h_len != 0:
            continue

        if (w_len - 2) * (h_len - 2) == yellow:
            return [w_len, h_len]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))