n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()

print(" ".join(map(str, nums)))

nums.sort(reverse=True)

print(" ".join(map(str, nums)))
