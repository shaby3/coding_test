N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
mapper = {
    "N": 0,
    "E": 1,
    "S": 2,
    "W": 3
}

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
cnt = 0
for dir_, dist_ in zip(dir, dist):
    d = mapper[dir_]

    for _ in range(dist_):
        x += dx[d]
        y += dy[d]
        cnt += 1
        if x == 0 and y == 0:
            print(cnt)
            break
    if x == 0 and y == 0:
        break
else:
    print(-1)