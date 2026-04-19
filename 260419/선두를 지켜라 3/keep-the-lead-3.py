N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
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

if time1[1] > time2[1]:
    prev = 1
elif time1[1] < time2[1]:
    prev = 2
else:
    prev = 3

ans = 0
for idx in range(2, len(time1)):
    if time1[idx] > time2[idx]:
        if prev != 1:
            ans += 1
        prev = 1
    elif time1[idx] < time2[idx]:
        if prev != 2:
            ans += 1
        prev = 2
    else:
        if prev != 3:
            ans += 1
        prev = 3

print(ans + 1)
# print(time1)
# print(time2)
