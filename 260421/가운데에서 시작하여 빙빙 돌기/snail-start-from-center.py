n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
sx, sy = n - 1, n - 1

grid[sx][sy] = n ** 2

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

d = 0

for i in range(1, n ** 2):
    nx, ny = sx + dx[d], sy + dy[d]

    if not in_range(nx, ny) or grid[nx][ny] != 0:
        d = (d + 1) % 4
    
    sx, sy = sx + dx[d], sy + dy[d]

    grid[sx][sy] = n ** 2 - i
    # print(sx, sy)

for row in grid:
    print(*row)

