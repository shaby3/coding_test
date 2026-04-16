OFFSET = 100
MAX_X = 200
MAX_Y = 200

n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
arr = [[0] * (MAX_Y + 1) for _ in range(MAX_X + 1)]

for i1, j1, i2, j2 in zip(x1, y1, x2, y2):
    for i in range(i1, i2):
        for j in range(j1, j2):
            arr[i][j] = 1

ans = 0
for i in range(MAX_X + 1):
    for j in range(MAX_Y + 1):
        if arr[i][j] == 1:
            ans += 1

print(ans)     