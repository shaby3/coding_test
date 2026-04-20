n, m = map(int, input().split())

# Please write your code here.
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

grid = [[0] * m for _ in range(n)]

grid[0][0] = 'A'

sx, sy = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for idx in range(1, n*m):
    nx, ny = sx + dx[d], sy + dy[d]

    if not in_range(nx, ny) or grid[nx][ny] != 0:
        d = (d + 1) % 4
    
    sx, sy = sx + dx[d], sy + dy[d]
    grid[sx][sy] = alpha[idx % 26]

for row in grid:
    print(*row)

