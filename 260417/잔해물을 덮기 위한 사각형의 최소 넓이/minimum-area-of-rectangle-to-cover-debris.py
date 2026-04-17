OFFSET = 1000
MAX_R = 2000

x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
mat = [[0 for _ in range(MAX_R)] for _ in range(MAX_R)]

for idx in range(2):
    i1, j1, i2, j2 = x1[idx] + OFFSET, y1[idx] + OFFSET, x2[idx] + OFFSET, y2[idx] + OFFSET

    for i in range(i1, i2):
        for j in range(j1, j2):
            mat[i][j] += (idx + 1)

min_i, max_i, min_j, max_j = MAX_R, 0, MAX_R, 0
flag = False
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j] == 1:
            flag = True
            min_i = min(i, min_i)
            max_i = max(i, max_i)
            min_j = min(j, min_j)
            max_j = max(j, max_j)

ans = (max_i - min_i + 1) * (max_j - min_j + 1)
if flag:
    print(ans)
else:
    print(0)
