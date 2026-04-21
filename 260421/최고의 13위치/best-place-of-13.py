n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

ans = 0
for i in range(n):
    for j in range(n - 2):
        acc = sum(grid[i][j:j+3])
        ans = max(ans, acc)
print(ans)