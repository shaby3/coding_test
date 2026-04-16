MAX_R = 1000 * 100 * 2

n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
cur_x = 1000 * 100

checked = [-1] * (MAX_R + 1)

for num, direction in zip(x, dir):
    # 만약 방향이 오른쪽으면
    if direction == "R":
        #한 타일씩 이동하면서 checked 1로 전환
        for next_x in range(cur_x, cur_x + num):
            checked[next_x] = 1
        # 현재 위치 갱신(cur_x + num - 1)
        cur_x += (num - 1)
    else:
        for next_x in range(cur_x - num + 1, cur_x + 1):
            checked[next_x] = 0
        cur_x -= (num - 1)

black_cnt = 0
white_cnt = 0
for color in checked:
    if color == 1:
        black_cnt += 1
    elif color == 0:
        white_cnt += 1

print(white_cnt, black_cnt)