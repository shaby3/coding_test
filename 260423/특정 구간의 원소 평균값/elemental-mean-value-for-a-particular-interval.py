n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0
for i in range(n):
    for j in range(i, n):
        mean_val = sum(arr[i:j + 1]) / (j - i + 1)
        if mean_val in arr[i: j + 1]:
            ans += 1
print(ans)