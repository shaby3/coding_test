N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

ans = float('inf')
for i in range(N - T + 1):
    tmp = 0
    for j in range(i, i + T):
        tmp += abs(arr[j] - H)
    ans = min(ans, tmp)
print(ans)