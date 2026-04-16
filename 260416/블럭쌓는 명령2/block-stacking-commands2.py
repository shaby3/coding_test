n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

blocks = [0] * n

for com in commands:
    s, e = com[0] - 1, com[1] - 1
    for idx in range(s, e + 1):
        blocks[idx] += 1

print(max(blocks))