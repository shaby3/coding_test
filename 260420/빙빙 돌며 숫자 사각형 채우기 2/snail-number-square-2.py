n, m = map(int, input().split())

# Please write your code here.
sx, sy = 0, 0
d = 0

grid = [[0] * m for _ in range(n)]

grid[sx][sy] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for idx in range(2, n * m + 1):
    nx, ny = sx + dx[d], sy + dy[d]

    if not in_range(nx, ny) or grid[nx][ny] != 0:
        d = (d + 1) % 4
    
    sx, sy = sx + dx[d], sy + dy[d]
    grid[sx][sy] = idx

for row in grid:
    print(*row)