n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
ans = 0
for i in range(n - 2):
    for j in range(i + 2, n):
        ans = max(ans, numbers[i] + numbers[j])
print(ans)