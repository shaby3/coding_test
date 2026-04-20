n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True

    return False

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for idx in range(4):
            ni = i + dx[idx]
            nj = j + dy[idx]
            
            if in_range(ni, nj) and grid[ni][nj] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)