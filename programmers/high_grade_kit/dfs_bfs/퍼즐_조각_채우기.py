dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_block(x, y, visited, table):
    n = len(table)
    block = [(x, y)]
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < n and 0 <= next_y < n:
            if table[next_x][next_y] == 1:
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    # 반환된 block 을 하나의 리스트로 합쳐준다.
                    block += get_block(next_x, next_y, visited, table)

    return block

def get_hole(x, y, visited, game_board):
    n = len(game_board)
    hole = [(x, y)]
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < n and 0 <= next_y < n:
            if game_board[next_x][next_y] == 0:
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    # 반환된 hole 을 하나의 리스트로 합쳐준다.

                    hole += get_hole(next_x, next_y, visited, game_board)

    return hole

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    table_visited = [[False] * n for _ in range(n)]
    game_board_visited = [[False] * n for _ in range(n)]

    # 추출한 블록의 리스트, 추출한 구멍 리스트
    blocks = []
    holes = []

    # dfs 를 활용해 각 블록의 좌표를 집합 자료형으로 뭉쳐 blocks 배열에 넣는다.
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                if not table_visited[i][j]:
                    block = get_block(i, j, table_visited, table)
                    blocks.append(set(block))

    # game_board 의 구멍을 찾는다
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                if not game_board_visited[i][j]:
                    hole = get_hole(i, j, game_board_visited, game_board)
                    holes.append(set(hole))


    # 이제 구멍과 블록을 90도 회전 시키면서 구멍과 블록이 맞는지 확인한다.


    return answer


print(solution(
    game_board=[[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
    table=[[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))
