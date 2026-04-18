n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
# 1000회씩 1000번 이동할 수 있기 때문에 시간 기록을 위한 배열의 크기는 1000 * 1000 으로 설정한다.
# 미리 배열의 크기를 기록할 필요가 잇을까? 매 이동 마다 arr에 하나씩 추가해주면 되는 구조 같은데
time1 = [0]
time2 = [0]

for direction, time in zip(d, t):
    if direction == "R":
        for _ in range(time):
            time1.append(time1[-1] + 1)
    else:
        for _ in range(time):
            time1.append(time1[-1] - 1)

for direction, time in zip(d2, t2):
    if direction == "R":
        for _ in range(time):
            time2.append(time2[-1] + 1)
    else:
        for _ in range(time):
            time2.append(time2[-1] - 1)

for idx in range(1, len(time2)):
    if time1[idx] == time2[idx]:
        print(idx)
        break
else:
    print(print(-1))