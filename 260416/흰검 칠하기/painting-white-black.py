cur_idx = 100000
MAX_R = 200000

n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
# 왼쪽 흰색 (0), 오른쪽 검정색 (1), 회색 (2)
last = [-1] * (MAX_R + 1)
count = [[0, 0] for _ in range(MAX_R + 1)]

for distance, direction in zip(x, dir):
    if direction == 'R': # 검정은 1
        for idx in range(cur_idx, cur_idx + distance):
            last[idx] = 1
            count[idx][1] += 1
        cur_idx += (distance - 1)
    else: # 흰색은 0
        for idx in range(cur_idx - distance + 1, cur_idx + 1):
            last[idx] = 0
            count[idx][0] += 1
        cur_idx -= (distance - 1)

black_cnt = 0
white_cnt = 0
gray_cnt = 0
for idx in range(MAX_R + 1):
    if count[idx][0] >= 2 and count[idx][1] >= 2:
        gray_cnt += 1
    elif last[idx] == 1:
        black_cnt += 1
    elif last[idx] == 0:
        white_cnt += 1

print(white_cnt, black_cnt, gray_cnt)

