def solution(s):
    answer = 1e15

    for x in range(1, len(s) // 2 + 1):
        comp_len = 0
        comp = ''
        count = 1

        for i in range(0, len(s) + 1, x):
            slice_str = s[i:i + x]
            if comp == slice_str:
                count += 1

            elif comp != slice_str:
                comp_len += len(slice_str)
                if count > 1:
                    comp_len += len(str(count))
                count = 1
                comp = slice_str

        answer = min(answer, comp_len)

    return answer

print(solution(s="abcabcdede"))
