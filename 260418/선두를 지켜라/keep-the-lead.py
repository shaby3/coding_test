n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
time1 = [0]
time2 = [0]

for velocity, time in zip(v, t):
    for _ in range(time):
        time1.append(time1[-1] + velocity)

for velocity, time in zip(v2, t2):
    for _ in range(time):
        time2.append(time2[-1] + velocity)

prev_state = 0
ans = 0
for idx in range(1, len(time1)):
    if time1[idx] > time2[idx]:
        state = 1
        if prev_state == 2:
            ans += 1
        prev_state = state
    elif time1[idx] < time2[idx]:
        state = 2
        if prev_state == 1:
            ans += 1
        prev_state = state

print(ans)