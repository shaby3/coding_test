OFFSET = 1000
MAX_H = 2000
MAX_W = 2000


x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
mat = [[0] * (MAX_W + 1) for _ in range(MAX_H + 1)]

for idx in range(3):
    i1, j1, i2, j2 = x1[idx], y1[idx], x2[idx], y2[idx]

    for x in range(i1, i2):
        for y in range(j1, j2):
            if idx < 2:
                mat[x][y] = 1
            else:
                mat[x][y] = 0

ans = 0
for i in range(MAX_H + 1):
    for j in range(MAX_W + 1):
        if mat[i][j] == 1:
            ans += 1

print(ans)