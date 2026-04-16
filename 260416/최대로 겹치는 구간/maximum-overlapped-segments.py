n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
blocks = [0] * 201

for x1, x2 in segments:
    x1 += 100
    x2 += 100

    for idx in range(x1, x2):
        blocks[idx] += 1

print(max(blocks))