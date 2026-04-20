n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
x, y = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr[x][y] = 1
d = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m
        

for idx in range(2, n * m + 1):
    nx, ny = x + dx[d], y + dy[d]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        d = (d + 1) % 4
    
    x += dx[d]
    y += dy[d]

    arr[x][y] = idx

for row in arr:
    print(*row)
