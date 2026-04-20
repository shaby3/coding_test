n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# M번에 걸쳐 색칠을 진행
# 편안한 상태.. 

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

grid = [[0] * n for _ in range(n)]

for r, c in points:
    r -= 1
    c -= 1

    grid[r][c] = 1

    cnt = 0
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = r + dx, c + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)
