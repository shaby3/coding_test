n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
people = list(zip(pos, alpha))

people.sort()

pos = [p[0] for p in people]
alpha = [p[1] for p in people]

dist = 0
for i in range(len(alpha)):
    for j in range(i + 1, len(alpha)):
        tmp = alpha[i: j + 1]
        h = tmp.count('H')
        g = tmp.count('G')

        if h == g or (h != 0 and g == 0) or  (h == 0 and g != 0):
            dist = max(dist, pos[j] - pos[i])
print(dist)
