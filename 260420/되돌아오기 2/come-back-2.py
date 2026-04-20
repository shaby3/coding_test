commands = input()

# Please write your code here.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

d = 0

x, y = 0, 0

cnt = 0
for com in commands:
    # 만약 F라면
        # 현재 방향으로 이동
    cnt += 1
    if com == 'F':
        x += dx[d]
        y += dy[d]
        if x == 0 and y == 0:
            print(cnt)
            break
    elif com == 'R':
        d = (d + 1) % 4
    elif com == 'L':
        d = (d - 1) % 4
else:
    print(-1)
    