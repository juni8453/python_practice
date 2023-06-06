def solution(s):
    all_count, zero_count = 0, 0

    while s != '1':
        all_count += 1
        c = s.count('1')
        zero_count += len(s) - c
        s = bin(c)[2:]

    return [all_count, zero_count]

print(solution(s='110010101001'))