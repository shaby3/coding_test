N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
bucket = [0] * 101
K = min(K, 50)

for c, p in zip(candy, pos):
    bucket[p] += c

ans = 0
for i in range(101 - 2 * K):
    ans = max(ans, sum(bucket[i: i + 2 * K + 1]))
print(ans)
