N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
sx, sy = N // 2, N // 2

d = 0

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = board[sx][sy]

for com in str:
    # 만약 왼쪽이라면?
        # d를 -1
    if com == "L":
        d = (d - 1) % 4

    # 만약 오른쪽이라면?
        # d를 + 1
    if com == "R":
        d = (d + 1) % 4

    # 만약 이동이라면?
        # d 기준으로 이동
    if com == "F":
        nx, ny = sx + dx[d], sy + dy[d]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        sx, sy = nx, ny
        ans += board[sx][sy]

print(ans)