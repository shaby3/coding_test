n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
# ans = 1
cnt = 1
for i in range(n - 1):
    if arr[i] != arr[i + 1]:
        cnt += 1
print(cnt)