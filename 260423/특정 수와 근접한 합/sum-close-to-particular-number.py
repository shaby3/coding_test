N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

ans = 9902

summation = sum(arr)
for i in range(N):
    for j in range(i + 1, N):
        cur_val = summation - arr[i] - arr[j]
        ans = min(ans, abs(S - cur_val))

print(ans)
