arr = list(map(int, input().split()))

# Please write your code here.
total_abil = sum(arr)
ans = float('inf')
for i in range(5):
    for j in range(i + 1, 5):
        team1 = arr[i] + arr[j]
        for k in range(5):
            if k == i or k == j:
                continue
            for l in range(k + 1, 5):
                if l == i or l == j:
                    continue
                team2 = arr[k] + arr[j]
                team3 = total_abil - team2 - team1
                if team2 == team3 or team1 == team2 or team3 == team1:
                    continue
                ans = min(ans, max(team1, team2, team3) - min(team1, team2, team3))

if ans == float('inf'):
    print(-1)
else:
    print(ans)
                