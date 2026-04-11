n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()

ans = -1

for i in range(n):
    j = 2*n - i - 1
    ans = max(ans, nums[i] + nums[j])

print(ans)
