board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
# 모든 좌표를 순회하며 우측, 우측대각선, 아래 방향을 탐색해서 
# 현재 좌표의 숫자와 다 같은 숫자인지 검증해서 맞으면 바둑돌과
# 중간 바둑돌의 좌표를 return 해주는 함수 작성

def check_row(si, sj):
    num = board[si][sj]
    if board[si][sj: sj + 5] == [num] * 5:
        return num, (si, sj + 2)
    return None

def check_col(si, sj):
    num = board[si][sj]
    if [board[si + d][sj] for d in range(5)] == [num] * 5:
        return num, (si + 2, sj)
    return None

def check_diag(si, sj):
    num = board[si][sj]
    for d in range(1, 5):
        ni, nj = si + d, sj + d
        if board[ni][nj] != num:
            return None
    return num, (si + 2, sj + 2)

def check_rev_diag(si, sj):
    num = board[si][sj]
    for d in range(1, 5):
        ni, nj = si + d, sj - d
        if board[ni][nj] != num:
            return None
    return num, (si + 2, sj - 2)

flag = True
# 가로부터
for i in range(19):
    for j in range(15):
        if board[i][j] != 0:
            val = check_row(i, j)
            if val is not None:
                num, (x, y) = val
                print(num)
                print(x + 1, y + 1)
                flag = False

for i in range(15):
    for j in range(19):
        if board[i][j] != 0:
            val = check_col(i, j)
            if val is not None:
                num, (x, y) = val
                print(num)
                print(x + 1, y + 1)
                flag = False

for i in range(15):
    for j in range(15):
        if board[i][j] != 0:
            val = check_diag(i, j)
            if val is not None:
                num, (x, y) = val
                print(num)
                print(x + 1, y + 1)
                flag = False

for i in range(15):
    for j in range(4, 19):
        if board[i][j] != 0:
            val = check_diag(i, j)
            if val is not None:
                num, (x, y) = val
                print(num)
                print(x + 1, y + 1)
                flag = False

if flag:
    print(0)
