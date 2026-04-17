n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
ans = 0

for i in range(n):
    # 만약 현재 값이 T보다 크면 cnt += 1, ans = max(ans, cnt)
    if arr[i] > t:
        cnt += 1
        ans = max(ans, cnt)
    # 만약 현재 값이 T보다 작거나 같으면 cnt = 1
    else:
        cnt = 0
print(ans)