dirs = input()

# Please write your code here.
# 북쪽: 0, 1 동쪽: 1, 0, 남쪽: 0, -1, 서쪽: -1, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
cx = 0
cy = 0
for dir in dirs:
    if dir == "L":
        d = (d - 1) % 4
    elif dir == "R":
        d = (d + 1) % 4
    else:
        cx += dx[d]
        cy += dy[d]


print(cx, cy)