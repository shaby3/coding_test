n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dir_dict = {"W":[-1, 0], "S": [0, -1], "N": [0, 1], "E": [1, 0]}

sx, sy = 0, 0
for dir1, dist1 in zip(dir, dist):
    dx, dy = dir_dict[dir1]

    sx += dx * dist1
    sy += dy * dist1

print(sx, sy)
