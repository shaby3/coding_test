n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
# A와 B의 시간별 위치를 기록할 배열 선언
time1 = [0]
time2 = [0]

# 각자 정해진 명령을 따라 이동하면서 매초 위치를 기록
for time, direction in zip(t, d):
    for _ in range(time):
        if direction == 'R':
            time1.append(time1[-1] + 1)
        elif direction == 'L':
            time1.append(time1[-1] - 1)

for time, direction in zip(t_b, d_b):
    for _ in range(time):
        if direction == 'R':
            time2.append(time2[-1] + 1)
        elif direction == 'L':
            time2.append(time2[-1] - 1)

prev1 = time1[0]
prev2 = time2[0]
ans = 0
for idx in range(max(len(time1), len(time2))):
    # 만약 두 로봇 다 움직이는 경우
    if idx < len(time1) and idx <len(time2):
        if prev1 != prev2 and time1[idx] == time2[idx]:
            ans += 1
        prev1 = time1[idx]
        prev2 = time2[idx]
    # 1만 움직일 수 있는 경우
    elif idx >= len(time2) and idx < len(time1):
        if prev2 != prev1 and prev2 == time1[idx]:
            ans += 1
        prev1 = time1[idx]
    # 2만 움직일 수 있는 경우
    elif idx < len(time2) and idx >= len(time1):
        if prev2 != prev1 and prev1 == time2[idx]:
            ans += 1
        prev2 = time2[idx]

print(ans)