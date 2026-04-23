n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
summation = sum(arr[:k])
ans = summation
for j in range(k, n):
    summation += arr[j]
    summation -= arr[j - k]
    ans = max(ans, summation)

print(ans)