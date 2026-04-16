n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
checked = [0] * (2001)

idx = 1000
for cx, cdir in zip(x, dir):
    # 만약 방향이 오른쪽이면
    if cdir == 'R':
        for i in range(idx, idx + cx):
            checked[i] += 1
        idx += cx
    else:
        for i in range(idx - cx, idx):
            checked[i] += 1
        idx -= cx

ans = 0
for cnt in checked:
    if cnt > 1:
        ans += 1

print(ans)
        