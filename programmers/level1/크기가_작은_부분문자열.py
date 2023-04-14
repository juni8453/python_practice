def solution(t, p):
    answer = 0
    t_size = len(t)
    p_size = len(p)

    # 3141592, 271 이라면 t 길이가 7, p 길이가 3 이므로 반복문이 4번 돌아야 out of index 가 발생하지 않는다.
    for i in range(t_size - p_size + 1):
        if int(t[i:i + p_size]) <= int(p):
            answer += 1

    return answer

print(solution("3141592", "271"))