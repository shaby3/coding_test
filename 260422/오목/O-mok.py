board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
# 모든 좌표를 순회하며 우측, 우측대각선, 아래, 좌측 대각선 아래 방향을 탐색해서 
# 현재 좌표의 숫자와 다 같은 숫자인지 검증해서 맞으면 바둑돌과
# 중간 바둑돌의 좌표를 return 해주는 함수 작성

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

def func():
    for i in range(len(board)):
        for j in range(len(board[0])):
            num = board[i][j]
            if not num:
                continue
            
            # 가로 체크
            for d in range(1, 5):
                nj = j + d
                if in_range(i, nj) and board[i][nj] == num:
                    pass
                else:
                    break
            else:
                return num, (i, j + 2)

            # 세로 체크
            for d in range(1, 5):
                ni = i + d
                if in_range(ni, j) and board[ni][j] == num:
                    pass
                else:
                    break
            else:
                return num, (i + 2, j)           

            # 우측 대각선 체크
            for d in range(1, 5):
                ni = i + d
                nj = j + d
                if in_range(ni, nj) and board[ni][nj] == num:
                    pass
                else:
                    break
            else:
                return num, (i + 2, j + 2)           

            # 좌측 대각선 체크
            for d in range(1, 5):
                ni = i + d
                nj = j - d
                if in_range(ni, nj) and board[ni][nj] == num:
                    pass
                else:
                    break
            else:
                return num, (i + 2, j - 2)
    return None

result = func()

if result is None:
    print(0)
else:
    num = result[0]
    coord = result[1]
    print(num)
    print(coord[0] + 1, coord[1] + 1)


