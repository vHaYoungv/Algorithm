def solution(game_board, table):
    answer = 0
    n = len(game_board)
    tmp_game_board = game_board[:]
    tmp_table = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp_table[i][j] = abs(table[i][j] - 1)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def dfs(x, y, graph):
        tmp.append((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    dfs(nx, ny, graph)

    # 회전
    def rotate_block(block):
        temp = []
        for i, j in block:
            temp.append((j, n - 1 - i))
        return temp

        # 채워야 하는 모양 구하기

    a = []
    for i in range(n):
        for j in range(n):
            if tmp_game_board[i][j] == 0:
                tmp = []
                tmp_game_board[i][j] = 1
                dfs(i, j, tmp_game_board)
                a.append(tmp)

    # 채울 모양 구하기
    b = []
    for i in range(n):
        for j in range(n):
            if tmp_table[i][j] == 0:
                tmp = []
                tmp_table[i][j] = 1
                dfs(i, j, tmp_table)
                b.append(tmp)

    print('---a')
    for row in a:
        print(row)

    print('---b')
    for row in b:
        print(row)

    # 구할 모양 마다 정렬하고,
    for i, Ablock in enumerate(a):
        Ablock = sorted(Ablock)
        print('---Ablock')
        print(Ablock)
        for Bblock in b:
            if len(Ablock) != len(Bblock):
                continue
            asdf = Bblock[:]
            tf = False
            for i in range(4):
                Bblock = sorted(Bblock)
                print('Bblock:', Bblock)
                for k in range(-n, n + 1):
                    for p in range(-n, n + 1):
                        tmpblock = list(map(lambda x: (x[0] + k, x[1] + p), Bblock))
                        if Ablock == tmpblock:
                            print('success', i, ':', tmpblock)
                            answer += len(Ablock)
                            tf = True
                            b.remove(asdf)
                        if tf: break
                    if tf: break
                if tf: break
                Bblock = rotate_block(Bblock)
            if tf: break

    return answer