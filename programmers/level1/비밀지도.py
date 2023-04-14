def solution(n, arr1, arr2):
    arr1_list = []
    arr2_list = []
    grid1 = []
    grid2 = []

    for i in arr1:
        change_bin = bin(i)[2:]
        if len(change_bin) < n:
            zero_count = n - len(change_bin)
            for i in range(zero_count):
                change_bin = '0' + change_bin

        arr1_list.append(change_bin)

    for i in arr2:
        change_bin = bin(i)[2:]
        if len(change_bin) < n:
            zero_count = n - len(change_bin)
            for i in range(zero_count):
                change_bin = '0' + change_bin

        arr2_list.append(change_bin)


    for i in range(n):
        split = list(arr1_list[i])
        grid1.append(split)

    for i in range(n):
        split = list(arr2_list[i])
        grid2.append(split)

    answer = []
    new_board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if grid1[i][j] == '1' or grid2[i][j] == '1':
                new_board[i][j] = '#'

            if grid1[i][j] == '0' and grid2[i][j] == '0':
                new_board[i][j] = ' '

        join = ''.join(new_board[i])
        answer.append(join)

    return answer

print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))
print(solution(6, [46,33,33,22,31, 50], [27,56,19,14,14, 10]))