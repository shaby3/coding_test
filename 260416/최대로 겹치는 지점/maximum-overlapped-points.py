n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
checked = [0] * 101

for x1, x2 in segments:
    for idx in range(x1, x2 + 1):
        checked[idx] += 1

print(max(checked))