n, k = map(int, input().split()) # n
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
placed = [0] * 10001

mapper = {
    "G": 1,
    "H": 2
}
for pos, char in zip(x, c):
    placed[pos] = mapper[char]

ans = 0
for i in range(1, 10001):
    ans = max(ans, sum(placed[i: i + k + 1]))

print(ans)