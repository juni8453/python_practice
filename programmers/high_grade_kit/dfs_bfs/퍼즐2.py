dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 블록 좌표를 추출하는 함수
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
                    block += get_block(next_x, next_y, visited, table)

    return block

# 구멍 좌표를 추출하는 함수
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
                    hole += get_hole(next_x, next_y, visited, game_board)

    return hole

# 블록을 회전하는 함수
def rotate_block(block):
    min_x, min_y = float('inf'), float('inf')
    for x, y in block:
        min_x = min(min_x, x)
        min_y = min(min_y, y)

    rotated_block = []
    for x, y in block:
        rotated_block.append((y - min_y + min_x, -(x - min_x) + min_y))

    return rotated_block

# 블록과 구멍이 맞는지 확인하는 함수
def is_fit(block, hole):
    for x, y in hole:
        if (x, y) not in block:
            return False
    return True

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    table_visited = [[False] * n for _ in range(n)]
    game_board_visited = [[False] * n for _ in range(n)]

    # 추출한 블록의 리스트
    blocks = []

    # dfs 를 활용해 각 블록의 좌표를 리스트 자료형으로 뭉쳐놓기
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not table_visited[i][j]:
                table_visited[i][j] = True
                blocks.append(get_block(i, j, table_visited, table))

    # 블록 회전 및 이동 후 적용 가능한 구멍 찾기
    for block in blocks:
        for _ in range(4):
            block = rotate_block(block)  # 블록 회전

            # 게임판에서 블록과 맞는 구멍 찾기
            for i in range(n):
                for j in range(n):
                    if game_board[i][j] == 0 and not game_board_visited[i][j]:
                        game_board_visited[i][j] = hole = get_hole(i, j, game_board_visited, game_board)  # 구멍 추출

                        if is_fit(block, hole):  # 블록과 구멍이 맞으면
                            answer += len(block)  # 블록 크기만큼 점수 추가

                            for x, y in block:  # 블록 좌표를 게임판에 반영
                                game_board[x][y] = 1

                            for x, y in hole:  # 구멍 좌표를 게임판에 반영
                                game_board[x][y] = 2
                                break  # 구멍에 맞는 블록을 찾았으면 다음 블록으로 넘어감
                        else:
                            continue  # 블록과 맞는 구멍을 찾지 못한 경우 회전을 반복함
                        break  # 구멍에 맞는 블록을 찾았으면 다음 블록으로 넘어감
    return answer



print(solution(
    game_board=[[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
    table=[[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))
