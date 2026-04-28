abilities = list(map(int, input().split()))

# Please write your code here.
total_abil = sum(abilities)

ans = 6000000
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            abil1 = abilities[i] + abilities[j] + abilities[k]
            abil2 = total_abil - abil1
            ans = min(ans, abs(abil1 - abil2))

print(ans)
