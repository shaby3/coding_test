ability = list(map(int, input().split()))

# Please write your code here

total_abil = sum(ability)

ans = float('inf')
for i in range(6):
    for j in range(i + 1, 6):
        team1 = ability[i] + ability[j]
        for k in range(6):
            if k == i or k == j:
                continue
            for l in range(k + 1, 6):
                if l == i or l == j:
                    continue
                team2 = ability[k] + ability[l]
                team3 = total_abil - team1 - team2
                ans = min(max(team1, team2, team3) - min(team1, team2, team3), ans)
print(ans)

