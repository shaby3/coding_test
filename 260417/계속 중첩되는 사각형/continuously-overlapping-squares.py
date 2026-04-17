offset = 100
max_r = 200

n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a + offset)
    y1.append(b + offset)
    x2.append(c + offset)
    y2.append(d + offset)

# Please write your code here.
mat = [[0 for _ in range(max_r)] for _ in range(max_r)]
for idx, (i1, j1, i2, j2) in enumerate(zip(x1, y1, x2, y2)):
    for i in range(i1, i2):
        for j in range(j1, j2):
            if idx % 2 == 0:
                mat[i][j] = 1
            else:
                mat[i][j] = 2

ans = 0
for i in range(max_r):
    for j in range(max_r):
        if mat[i][j] == 2:
            ans += 1

print(ans)



