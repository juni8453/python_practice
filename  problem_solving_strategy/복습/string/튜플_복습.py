# 처음 풀이 (틀린 풀이)
# def solution(s):
#     answer = []
#
#     # 문자열 s 의 바깥 중괄호를 제거한다.
#     s = s[1:-1]
#     s = eval(s)
#
#     # eval() 을 활용해 set() -> list() 로 변환
#     my_list = []
#     for i in s:
#         my_list.append(list(i))
#
#     while len(my_list) != 0:
#         min_len_list = min(my_list, key=len)
#
#         for i in min_len_list:
#             if answer.count(i) > 0: # 이미 있다면
#                 continue
#
#             answer.append(i)
#
#         my_list.remove(min_len_list)
#
#     return answer
#
#
# print(solution('{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}')) # (2, 3, 4, 1)
# # print(solution('{{123}}')) # (123)


# 두 번째 풀이 (맞는 풀이)
def solution(s):
    answer = []
    s = s[2:-2]
    elements = s.split('},{')

    my_list = []
    for e in elements:
        inner_list = e.split(',')
        inner_list = list(map(int, inner_list))
        my_list.append(inner_list)

    while len(my_list) != 0:
        min_len_list = min(my_list, key=len)

        for i in min_len_list:
            if answer.count(i) > 0:  # 이미 있다면
                continue

            answer.append(i)

        my_list.remove(min_len_list)

    return answer


print(solution('{{123}}'))  # (123)
