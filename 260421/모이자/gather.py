n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
ans = 10000 * 100
for dest in range(n):
    total_dist = 0
    for start in range(n):
        dist = abs(dest - start)
        total_dist += dist * A[start]
    
    ans = min(ans, total_dist)
print(ans)